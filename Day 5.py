import csv
import re
import numpy as np
import copy
regnum = "\\d+"

with open("input.txt", "r") as f:
	reader = csv.reader(f)
	data = list(reader)

lib = [[],[],[],[],[],[],[],[]]
z = 0
for i in data:
	if i:
		templib = []
		for j in re.finditer(regnum, i[0]):
			templib.append(j.group())
		if templib:
			lib[z].append(templib)
	else:
		z += 1	

def newArray(oldArray,check,diff):
	tempSeeds = []
	newSeeds = []
	for p in oldArray:
		if min(p) < min(check) and max(p) > max(check):

			tempSeeds.append([min(p),min(check)-1])
			newSeeds.append([min(check)+diff,max(check)+diff])
			tempSeeds.append([max(check)+1,max(p)])
		elif min(p) >= min(check) and max(p) <= max(check):

			newSeeds.append([min(p)+diff,max(p)+diff])
		elif min(p) <= max(check) and max(p) > max(check):

			newSeeds.append([min(p)+diff,max(check)+diff])
			tempSeeds.append([max(check)+1,max(p)])
		elif max(p) >= min(check) and min(p) < min(check):

			tempSeeds.append([min(p),min(check)-1])
			newSeeds.append([min(check)+diff,max(p)+diff])
		else:

			tempSeeds.append(p)
	return tempSeeds,newSeeds
total = []
for j,i in enumerate(lib[0][0]):
	z = 0
	actualSeeds=None
	print("Start Loop 1")
	if j%2 == 0:
		actualSeeds = [[int(lib[0][0][j]),int(lib[0][0][j])+int(lib[0][0][j+1])]]
	if actualSeeds:
		# If there is anything in the seed array do stuff
		temp1 = actualSeeds

		for k in lib[1:8]:
			print("Check")
			newCheck = []
			for m in k:
				# Current checks
				if temp1:
					temp2,temp3 = newArray(temp1,[int(m[1]),int(m[2])+(int(m[1])-1)],int(m[0])-int(m[1]))
					temp1 = temp2[:]
					newCheck.extend(temp3[:])
			temp1 = temp1+newCheck

			# Next conversion
		total.extend(temp1)
		total.extend(newCheck)
		print("End Loop 1")

z = None
for i in total:
	if not z or min(i) < z:
		z = min(i)
print(z)
