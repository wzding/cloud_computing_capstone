from __future__ import print_function
import sys
from pyspark import SparkContext

if __name__ == "__main__":
	sc = SparkContext(appName="task_1_sorting")
	file = sc.textFile(sys.argv[1])
	rdd = file.cache()
	top_10 = rdd.map(lambda line: line.split())\
			    .filter(lambda tuple: len(tuple) == 2)\
			    .map(lambda tuple: (int(tuple[1] tuple[0]))\
			   	.sortByKey(ascending=False).take(10)
	top_10.saveAsTextFile(sys.argv[2])
	sc.stop()