import org.apache.spark._
import org.apache.log4j._
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.expressions.WindowSpec
import org.apache.spark.sql.functions.col
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types.DateType
import org.apache.spark.sql.functions.dense_rank

/** Count up how many of each star rating exists in the MovieLens 100K data set. */
object TopURLs {

  /** Our main function where the action happens */
  def main(args: Array[String]) {

    // Set the log level to only print errors
    Logger.getLogger("org").setLevel(Level.ERROR)

    // Create a SparkContext using every core of the local machine, named RatingsCounter
    //val sc = new SparkContext("local[*]", "TopURLs")

    // Load up each line of the ratings data into an RDD
    // val lines = sc.textFile("data/NASA_access_log_10rows")

    val spark = SparkSession
      .builder
      .appName("TopURLs")
      .master("local[*]")
      .getOrCreate()

    // Load each line of the source data into an Dataset
    import spark.implicits._
    val ds = spark.read
      .option("header", "false")
      .option("inferSchema", "false")
      .text("data/NASA_access_log_Jul95")

    // Regular expressions to extract pieces of Apache access log lines
    val contentSizeExp = "\\s(\\d+)$"
    val statusExp = "\\s(\\d{3})\\s"
    val generalExp = "\"(\\S+)\\s(\\S+)\\s*(\\S*)\""
    val timeExp = "\\[(\\d{2}/\\w{3}/\\d{4}:\\d{2}:\\d{2}:\\d{2} -\\d{4})]"
    val hostExp = "(^\\S+\\.[\\S+\\.]+\\S+)\\s"

    // Apply these regular expressions to create structure from the unstructured text
    val logsDF = ds.select(regexp_extract(col("value"), hostExp, 1).alias("host"),
    regexp_extract(col("value"), timeExp, 1).alias("timestamp"),
    regexp_extract(col("value"), generalExp, 1).alias("method"),
    regexp_extract(col("value"), generalExp, 2).alias("endpoint"),
    regexp_extract(col("value"), generalExp, 3).alias("protocol"),
    regexp_extract(col("value"), statusExp, 1).cast("Integer").alias("status"),
    regexp_extract(col("value"), contentSizeExp, 1).cast("Integer").alias("content_size"))
    
    val logsDF1 = logsDF.filter("endpoint != ''")
    val logsDF2 = logsDF1.withColumn("date", substring(col("timestamp"),1,11))

    //logsDF2.show()

    //val newDF = logsDF.withColumn("date", col("timestamp").cast(DateType))
    
    //logsDF2.printSchema
    //newDF.show()
    val numOfRowsToReturn = 5

    //create a window partitioned by date and count columns
    val overDateCount = Window.partitionBy($"date").orderBy($"count".desc)

    val countDF = logsDF2.groupBy("endpoint", "date").count()
    val rankedDF = countDF.withColumn("ranking", dense_rank.over(overDateCount)).filter(col("ranking") <= numOfRowsToReturn)
    val topUrlDF = rankedDF.select("*").orderBy(col("date").asc, col("count").desc)
    topUrlDF.show(false) 

  }

}

