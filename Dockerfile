FROM ubuntu:latest

RUN apt update
RUN apt install default-jdk -y
RUN apt install scala -y
RUN apt install wget -y

# download and unzip spark distribution
RUN mkdir download && \
    cd download && \
    wget https://archive.apache.org/dist/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz && \
    tar -xvf spark-3.2.1-bin-hadoop3.2.tgz

# set up Apache Spark
RUN cd /opt && \
    mkdir spark && \
    mv /download/spark-3.2.1-bin-hadoop3.2/* ./spark

#RUN echo "export SPARK_HOME=/opt/spark" >> ~/.profile
#RUN export SPARK_HOME=/opt/spark && \
#    echo "export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin" >> ~/.profile && \
#    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
    #. ~/.profile && \
#RUN /opt/spark/sbin/start-master.sh

# start spark mastrer and worker processes
#RUN start-master.sh
#RUN /opt/spark/sbin/start-worker.sh spark://$HOSTNAME:7077

#WORKDIR /src/main/
#COPY HelloWorld.scala .
#RUN scalac HelloWorld.scala
#CMD ["scala", "HelloWorld"]

ENV SPARK_HOME /opt/spark
ENV RUN_DIR /app/ratings-counter/run
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin:$RUN_DIR
#SHELL ["/bin/bash","-c", "source ~/.profile"]
#RUN source /root/.profile

COPY ratings-counter /app/ratings-counter
RUN cd /app/ratings-counter && \
    mkdir run
RUN mv /app/ratings-counter/start-spark-job.sh $RUN_DIR && \
    cd $RUN_DIR && \
    chmod 755 start-spark-job.sh
#SHELL ["/bin/bash","-c"]
#CMD ["start-spark-job.sh"]
