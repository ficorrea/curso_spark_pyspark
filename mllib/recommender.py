# -*- coding: utf-8 -*-

import findspark
findspark.init('/home/spark/spark-2.4.0-bin-hadoop2.7')

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('recm').getOrCreate()
