#!/bin/python3

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
print(sum([1 for x in apple if(a+x>=s and a+x<=t)]))
print(sum([1 for x in orange if(b+x>=s and b+x<=t)]))