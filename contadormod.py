import sys, re
import pySpark
from collections import Counter
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("gs://desafiodata/toystory1.txt").flatMap(lambda line: line.split(" "))
    words = re.sub(r'\(.+\)|<.+?>|\{.+\||\[.+?\]| \*.+?\* |\] | ! |\}', '', words)
    
    wordlist = words.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)


    result.saveAsTextFile("gs://desafiodata/resultadotoy.txt")
