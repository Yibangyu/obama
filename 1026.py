#!/usr/bin/python

import math

row_line = input()

N,C = row_line.split()

N = int(N)

print(C*N)


for i in range(0,math.ceil(N/2) -2 ):
	print(C,end='')
	print(' '*(N-2),end='')
	print(C)

print(C*N)



