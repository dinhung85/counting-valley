import math
import os
import random
import re
import sys
import pandas as pd


s = 'DDUUDDDUDUUDUDDDUUDDUDDDUDDDUDUUDDUUDDDUDDDUDDDUUUDUDDDUDUDUDUUDDUDUDUDUDUUUUDDUDDUUDUUDUUDUUUUUUUUU'
n = len(s)

ud = {"U":1,"D":-1}

# Complete the countingValleys function below.
ud = {"U":1,"D":-1}

# Complete the countingValleys function below.
def countingValleys(n, s):
	s_list = list(s)
	n_list =[]
	m = 0
	sl=0
	sea_level = [0]
	for i in s_list:
		n_list.append(ud[i])
		sl = sl + ud[i]
		sea_level.append(sl)
		sea_level_string = ''.join(str(e) for e in sea_level)
	df = pd.DataFrame({'col':sea_level})
	df.plot()
	print (df)
	m = sea_level_string.count('-10')
	print(sea_level_string, m)
	sea_level_string = sea_level_string.replace('-10','___')
	print(sea_level_string, m)
	return m


		# print(n_list,sea_level)

countingValleys(n,s)
