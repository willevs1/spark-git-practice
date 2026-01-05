from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
import os

spark = SparkSession.builder.appName("Test").getOrCreate()

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_path, "data", "sample.csv")

df = spark.read.option("header", True).option("inferSchema", True) \
    .csv(data_path)

df.show()

chicken = 1

df.groupBy("dept").agg(avg("salary").alias("avg_salary")).show()

spark.stop()

