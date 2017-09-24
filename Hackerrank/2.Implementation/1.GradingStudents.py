#!/bin/python3

import sys

k=int(input())
n=[int(input()) for x in range(0,k)]

for a in n:
    if (a>=38 and (5-(a%5))<3):
        print(a+(5-(a%5)))
    else:
        print(a)