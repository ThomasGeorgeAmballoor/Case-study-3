# from pyspark.sql import SparkSession
# spark = SparkSession.builder.appName('Sales Analysis').getOrCreate()
# df1 = spark.read.format("csv").option("header","True").option("InferSchema","True").load("F:\Case_Study_AI_Compute\Bank_Transaction_Fraud_Detection.csv")
import os
import shutil

print("JAVA_HOME:", os.environ.get("JAVA_HOME"))
print("SPARK_HOME:", os.environ.get("SPARK_HOME"))
print("PYSPARK_PYTHON:", os.environ.get("PYSPARK_PYTHON"))
print("PYSPARK_DRIVER_PYTHON:", os.environ.get("PYSPARK_DRIVER_PYTHON"))

print("java:", shutil.which("java"))
print("python:", shutil.which("python"))
