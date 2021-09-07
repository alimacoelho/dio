   with open('resultado_parcial.txt', 'r') as file:
    data = file.read().replace('\n', '')

    print(data)
    words = data
    wordlist = words.split()
    wordcount = Counter(wordlist)
    result = str(wordcount.most_common(10))
    result = re.sub( '\[|]|\(| [),]', '', result)
    result = re.sub( '\),','\n',result)
    result = re.sub( '[)]', '', result)

    resultado = open("resultado.txt", "w")
    resultado.write(result)
    resultado.close()

