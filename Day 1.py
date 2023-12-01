import numpy as np
import pandas as pd
from string import ascii_letters as characters
remove_letters = str.maketrans("","", characters)
data = pd.read_csv("input.txt",header=None)
total = 0
replacementDic= {
	"seven":"7",
	"four":"4",
	"six":"6",
	"eightwo":"82",
	"eightwone":"821",
	"twone":"21",
	"oneight":"18",
	"threeight":"38",
	"nineight":"98",
	"fiveight":"58",
	"eighthree":"83",
	"nine":"9",
	"five":"5",
	"one":"1",
	"two":"2",
	"three":"3",
	"eight":"8"
}
data[0] = data[0].replace(replacementDic, regex=True)
for i in data[0]:
	number = i.translate(remove_letters)
	z = number[0] + number[-1]
	total += int(z)
print(total)