#!/bin/python3

import sys


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
diagA=0
diagB=0
for i in range(0,len(a)):
    diagA+=a[i][i]
    diagB+=a[i][n-1-i]

print(abs(diagA-diagB))