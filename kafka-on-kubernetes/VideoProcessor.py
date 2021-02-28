import logging
from pyspark.sql import SparkSession


def run_spark_job(spark):
  df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "a63543f6db37a4e38bf6f3bc7af62006-312144799.ap-northeast-2.elb.amazonaws.com:9092", \
            "af2545fc9bf214ecd9bb281e4eeb2784-651446329.ap-northeast-2.elb.amazonaws.com:9092", \
            "a8c647669c5d64602a8a367098550827-409143955.ap-northeast-2.elb.amazonaws.com:9092") \
    .option("subscribe", "nomask-test5") \
    .option("startingOffsets", "earliest") \
    .option("maxOffsetsPerTrigger", 10) \
    .option("stopGracefullyOnShutdown", "true") \
    .load()

  # Show schema for the incoming resources for checks
  df.printSchema()


if __name__ == "__main__":
  logger = logging.getLogger(__name__)

  spark = SparkSession \
    .builder \
    .master("local[*]") \
    .appName("StructuredStreamingSetup") \
    .getOrCreate()

  logger.info("Spark started")

  run_spark_job(spark)

  spark.stop()