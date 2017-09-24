#!/bin/python3

import sys

def getRecord(s):
    l=s[0]
    h=s[0]
    lr=0
    hr=0
    for x in s:
        if x>h:
            h=x
            hr+=1
        if x<l:
            l=x
            lr+=1
    print("{} {}".format(hr,lr))

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
