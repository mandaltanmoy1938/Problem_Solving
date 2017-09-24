#!/bin/python3

import sys


n = int(input().strip())
s=""
for i in range(n):
    s=s+" "
s=list(s)
for i in range(1,n+1):
    s[n-i]='#'
    print(''.join(s))
    s=list(s)