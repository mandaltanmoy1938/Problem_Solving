#!/bin/python3

import sys

def timeConversion(s):
    s=s.split(':')
    hh=0
    if "PM" in s[2]:
        if(s[0]!="12"):
            hh=(int(s[0])) + 12
            s[0]=str(hh)
    elif "AM" in s[2]:
        if(s[0]=="12"):
            s[0]="00"
    s[2]=s[2].replace("AM","")
    s[2]=s[2].replace("PM","")
    s=':'.join(s)
    return s

s = input().strip()
result = timeConversion(s)
print(result)