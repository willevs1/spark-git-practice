from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

spark = SparkSession.builder.appName("Test").getOrCreate()

df = spark.read.option("header", True).option("inferSchema", True) \
    .csv("../data/sample.csv")

df.show()

df.groupBy("dept").agg(avg("salary").alias("avg_salary")).show()

spark.stop()
