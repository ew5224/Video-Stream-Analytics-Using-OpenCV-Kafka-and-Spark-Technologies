import logging
from pyspark.sql import SparkSession


def run_spark_job(spark):
  df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "a033c466eb00e4ad4944fbdb9601e68c-1925513909.ap-northeast-2.elb.amazonaws.com:9092, \
            a63ce823295da40559f25beb8ce48147-1966972725.ap-northeast-2.elb.amazonaws.com:9092, \
            aedac70e74b6e44eb831a820b2b3c1e0-68828054.ap-northeast-2.elb.amazonaws.com:9092") \
    .option("subscribe", "nomask-test") \
    .load()


  # Show schema for the incoming resources for checks
  df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")


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