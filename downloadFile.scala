import sys.process._
//import java.net.URL
import java.net.{HttpURLConnection, URL}
import java.io.{FileReader,FileWriter}
import java.io.FileNotFoundException
import java.io.IOException
import java.io._
import java.net._
import java._
import scala.collection.JavaConverters._
import scala.language.postfixOps
import scala.util.control._

object downloadFile {
  def main(args: Array[String]) {

    if (args.size == 0)
        println("Please specify URL")
    else {
        println("arg 0:" + args(0))
        //println("arg 1:" + args(1))
        val urlOfFileToDownload = args(0)
        //val outputFileName = args(1)
        val index = urlOfFileToDownload.lastIndexOf("/")
        val downloadFileName = urlOfFileToDownload.substring(index+1)
        println("index:" + index)
        println("file to download: " + downloadFileName)
        val outputFileName = downloadFileName
        val url = new URL(urlOfFileToDownload)

        val connection = url.openConnection().asInstanceOf[HttpURLConnection]
        connection.setConnectTimeout(5000)
        connection.setReadTimeout(5000)
        //connection.setDoOutput(false);
        connection.connect()

        /*
        if (connection.getResponseCode >= 400) {
          println("error: " + connection.getResponseCode)
          connection.disconnect()
        }

        
        else
          println("downloading...")
          url #> new File(fileName) !! 
        */
       try {
          if (connection.getResponseCode >= 400) {
            println("error downloading the file - HTTP error code: " + connection.getResponseCode)
            connection.disconnect()
        }
          else {
            println("downloading...")
            url #> new File(outputFileName) !!
          }
       }
       catch {
         case e: java.io.IOException => println("Had an IOException trying to read that file")
         case e: java.lang.RuntimeException => println("Runtime exception")
         case e: java.io.FileNotFoundException => println("Couldn't find that file.")
         case e: java.net.SocketTimeoutException => println("Connection timeout")
       }
    }
  }
}

