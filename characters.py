r = open ("resultado_part-00000.txt",'r')
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
f = open("dict.txt", "w")
f.write("{\n")
for k in total_sorted.keys():        
	f.write(F"'{k}': '{total_sorted[k]}',\n")  
		
f.write("}")
f.close() 
