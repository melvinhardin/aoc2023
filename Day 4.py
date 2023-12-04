import csv
import re
import numpy as np
regnum = "(?!\\d+:)\\d+"

with open("input.txt", "r") as f:
	reader = csv.reader(f, delimiter="|")
	data = list(reader)

dig = []
for i in data:
	cardtemp = []
	for j in i:
		digtemp = []
		for p in re.finditer(regnum, j):
			digtemp.append(p.group(0))
		cardtemp.append(digtemp)
	dig.append(cardtemp)
total = 0

for i in dig:
	z = -1
	for j in i[0]:
		if j in i[1]:
			z += 1
	if z != -1:
		total += 2**z
print(total)

counter = np.ones(len(dig))
for l,i in enumerate(dig):
	z = 0
	for j in i[0]:
		if j in i[1]:
			z += 1
	counter[l+1:l+1+z] = counter[l+1:l+1+z] + 1*counter[l]
print(np.sum(counter))
