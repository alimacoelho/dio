import sys, re
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")

words = sc.textFile("gs://desafio_dataproc123/toystory1.txt").flatMap(lambda line: line.split(" "))
words = re.sub(r'\(.+\)', '', words)
words = re.sub(r'<.+?>', '', words)

words = re.sub(r'\{.+\|', '', words)
words = re.sub(r'}', '', words)
words = re.sub(r'\[.+?\]', '', words)
words = re.sub(r'\*.+?\*', '', words)
words = re.sub(r'\]', '', words)
   
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    wordCounts.saveAwordsextFile("gs://desafio_dataproc123/resultado")
