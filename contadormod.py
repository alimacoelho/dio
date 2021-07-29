import sys, re
from collections import Counter
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words.toLocalIterator.mkString
    words = re.sub(r'\(.+\)|<.+?>|\{.+\||\[.+?\]| \*.+?\* |\] | ! |\}', '', words)
    
    wordlist = words.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)


    result.saveAsTextFile("gs://desafiodata/resultadotoy.txt")
