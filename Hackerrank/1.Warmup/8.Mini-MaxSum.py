#!/bin/python3

import sys
from collections import OrderedDict
arr = list(map(int, input().strip().split(' ')))
dictionary=dict()
sumAr=sum(arr)
minSum=0
maxSum=0
for i in arr:
    dictionary[i]=1
    
dictionary=OrderedDict(sorted(dictionary.items()))

for i,item in enumerate(dictionary):
    if i==0 and i==(len(dictionary)-1):
        maxSum=sumAr-item
        minSum=sumAr-item
    elif i==0:
        maxSum=sumAr-item
    elif i==(len(dictionary)-1):
        minSum=sumAr-item
        

print("{} {}".format(minSum,maxSum))