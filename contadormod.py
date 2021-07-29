import sys, re
from collections import Counter
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    
    
    txtfile = sc.textFile("gs://desafiodata/toystory1.txt")
    
  
    lines = re.sub(r'\(.+\)|<.+?>|\{.+\||\[.+?\]| \*.+?\* |\] | ! |\}', '', txtfile)
    
    wordlist = lines.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)


    result.saveAsTextFile("gs://desafiodata/resultadotoy.txt")
