import csv
import re

regsym = "[^.\\d\\*]"
regdig = "\\d+"
regdigsep = "\\d"
regstar = "[*]"
with open("input.txt", "r") as f:
	reader = csv.reader(f)
	data = list(reader)
dig = []
sym = []
star= []
total = 0
def getnumbers(place,array):
	test = 0
	test = re.finditer(regdig,data[array][0])
	for i in test:
		if place >= i.start() and place <= i.end():
			number = int(data[array][0][i.start():i.end()])
			data[array][0] = data[array][0][:i.start()] + "." * (i.end()-i.start()) + data[array][0][i.end():]
			return number
	return 0
for i in data:
	for j in i:
		symtemp = []
		digtemp = []
		startemp = []
		for p in re.finditer(regsym, j):
			symtemp.append(p.start())
		for p in re.finditer(regdigsep, j):
			digtemp.append(p.start())
		for p in re.finditer(regstar, j):
			startemp.append(p.start())	
		sym.append(symtemp)
		dig.append(digtemp)
		star.append(startemp)
total = 0
gears = []
for i,j in enumerate(data):
	if star[i]:
		for j in star[i]:
			print(j)
			if j-1 in dig[i]:
				gears.append(getnumbers(j-1,i)) 
			if j+1 in dig[i]:
				gears.append(getnumbers(j+1,i)) 
			if j in dig[i-1] and i != 0:
				gears.append(getnumbers(j,i-1)) 
			if j-1 in dig[i-1] and i != 0:
				gears.append(getnumbers(j-1,i-1))
			if j+1 in dig[i-1] and i != 0:
				gears.append(getnumbers(j+1,i-1))
			if i != len(dig)-1 and j in dig[i+1]:
				gears.append(getnumbers(j,i+1)) 
			if i != len(dig)-1 and j-1 in dig[i+1]:
				gears.append(getnumbers(j-1,i+1))
			if i != len(dig)-1 and j+1 in dig[i+1]:
				gears.append(getnumbers(j+1,i+1))
			gears = [z for z in gears if z != 0]
			p = 1
			print(gears)
			if len(gears) > 1:
				for l in gears:
					p = p*l
			else:
				p = 0
			total += p
			gears = []
			p = 1
print(total)

# for i,j in enumerate(data):
# 	if sym[i]:
# 		for j in sym[i]:
# 			if j-1 in dig[i]:
# 				total += getnumbers(j-1,i)
# 			if j+1 in dig[i]:
# 				total += getnumbers(j+1,i)
# 			if j in dig[i-1] and i != 0:
# 				total += getnumbers(j,i-1)
# 			if j-1 in dig[i-1] and i != 0:
# 				total += getnumbers(j-1,i-1)
# 			if j+1 in dig[i-1] and i != 0:
# 				total += getnumbers(j+1,i-1)
# 			if i != len(dig)-1 and j in dig[i+1]:
# 				total += getnumbers(j,i+1)
# 			if i != len(dig)-1 and j-1 in dig[i+1]:
# 				total += getnumbers(j-1,i+1)
# 			if i != len(dig)-1 and j+1 in dig[i+1]:
# 				total += getnumbers(j+1,i+1)
