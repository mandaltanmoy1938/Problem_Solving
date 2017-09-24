#!/bin/python3

import sys


n = int(input().strip())
i=0
j=0
k=0
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for a in arr:
    if a>0:
        i+=1
    elif a<0:
        j+=1
    elif a==0:
        k+=1
print('{:.6f}\n{:.6f}\n{:.6f}'.format( (i/n), (j/n), (k/n)))