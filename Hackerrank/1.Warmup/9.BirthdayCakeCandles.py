#!/bin/python3

import sys
from collections import OrderedDict

def birthdayCakeCandles(n, ar):
    # Complete this function
    dictionary=dict()
    for i in ar:
        if i in dictionary:
            dictionary[i]+=1
        else:
            dictionary[i]=1
    dictionary=OrderedDict(sorted(dictionary.items()))
    #print(dictionary)
    for i,item in enumerate(dictionary):
        if i==(len(dictionary)-1):
            return dictionary[item]
    

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
