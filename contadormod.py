import sys, re
from collections import Counter

if __name__ == "__main__":
  
    s = open ('toystory1.txt','r')
    words = s.read()
    words = re.sub(r'\(.+\)|<.+?>|\{.+\||\[.+?\]| \*.+?\* |\] | ! |\}', '', words)
    
    wordlist = words.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)


    f = open("resultados.txt", "w")
    f.write(result)
    f.close()
