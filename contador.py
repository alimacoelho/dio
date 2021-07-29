import sys
from pyspark import SparkContext, SparkConf
if __name__ == "__main__":
    sc = SparkContext("local","PySpark Exemplo - Desafio Dataproc")
    words = sc.textFile("gs://desafiodata/toystory.txt").flatMap(lambda line: line.split(" "))
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b).sortBy(lambda a:a[1], ascending=False)
    wordCounts.saveAsTextFile("gs://desafiodata/resultado")
    r = open ("gs://desafiodata/resultado",'r')
    resultado = r.readlines()
    characters = ['Buzz', 'Woody', 'Jessie', 'Bullseye', 'Slinky', 'Rocky', 'Wheezy', 'Pete', 'Bo', 'Potato' , 'Rex', 'Hamm', 'Sarge', 'RC', 'Andy', 'Sid', 'Hannah', 'Zurg']

    total = {}
    final = []
    o = 0
    for char in characters:
        for word in resultado:

            if char in word:
                final.append(word)
                n = re.search("\d\d\d|\d\d|\d", word)
                m = int(n.group(0))
                o = m+o
                total[char] = o
        o = 0

        total_sorted = {k: v for k, v in sorted(total.items(), key=lambda x: x[1], reverse=True)}
        total_sorted.saveAsTextFile("gs://desafiodata/nomes")
