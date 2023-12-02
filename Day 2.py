import csv
import re

colors = ['red','green','blue']

with open("input.txt", "r") as f:
	reader = csv.reader(f, delimiter=";")
	data = list(reader)

for z,i in enumerate(data):
	data[z] = [re.sub(r'Game \d:','',j) for j in i]
games = []

def colorNumEx(text,col):
	z = []
	for i in col:
		p = 0
		if not re.findall('\d+ '+i,text):
			p = 0
		else:
			p = int(re.findall('\d+',re.findall('\d+ '+i,text)[0])[0])
		z.append(p)

	return z


for y,i in enumerate(data):
	subgame = []
	for j in i:

		subgame.append(colorNumEx(j,colors))
	games.append(subgame)
z = 0
total = 0
for i in games:
	z += 1
	check = True
	for j in i:
		if j[0] < 13  and j[1] < 14 and j[2] < 15 and check:
			check = True
		else:
			check = False
	if check:
		total += z
print(total)
total = 0
for i in games:
	x = [0,0,0]
	for j in i:
		if j[0] > x[0]:
			x[0] = j[0]
		if j[1] > x[1]:
			x[1] = j[1]
		if j[2] > x[2]:
			x[2] = j[2]
	total += x[0]*x[1]*x[2]
print(total)
