import csv
import re
import numpy as np 

regnum = "\\d+"

with open("input.txt", "r") as f:
	reader = csv.reader(f)
	data = list(reader)

x = [44806572]
d = [208158110501102]

for i in data:
	for j in re.finditer(regnum, i[0]):
		int(j.group())


winners = []
for p,i in enumerate(x):
	l = 0
	#time = range(0,int(i))
	result = [(z*(int(i)-z)) for z in range(0,int(i)+1)]
	for k in result:
		if k > d[p]:
			l += 1
	winners.append(l)
print(np.prod(np.array(winners)))


