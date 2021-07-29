    
    s = open ('toystory1.txt','r')
    words = s.read()
    words = re.sub(r'\(.+\)', '', words)
    words = re.sub(r'<.+?>', '', words)
    words = re.sub(r'\{.+\|', '', words)
    words = re.sub(r'}', '', words)
    words = re.sub(r'\[.+?\]', '', words)
    words = re.sub(r'\*.+?\*', '', words)
    words = re.sub(r'\]', '', words)
    words = re.sub(r'!', '', words)
   



    f = open("toystory.txt", "w")
    f.write(words)
    f.close()
