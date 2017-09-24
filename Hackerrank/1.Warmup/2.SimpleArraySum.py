#!/bin/python3

import sys

def simpleArraySum(n, ar):
    # Complete this function
    x=0
    for a in ar:
        x+=a
    return x

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)