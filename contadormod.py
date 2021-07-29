import sys, re
import txt
from collections import Counter
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    
lines = []   
with open(r'gs://desafiodata/toystory1.txt','r') as txtfile:
    txtreader = txt.reader(txtfile)
    for line in txtreader:
        lines.append(line)
    
    
    
    lines.toLocalIterator.mkString
    lines = re.sub(r'\(.+\)|<.+?>|\{.+\||\[.+?\]| \*.+?\* |\] | ! |\}', '', lines)
    
    wordlist = lines.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)


    result.saveAsTextFile("gs://desafiodata/resultadotoy.txt")
