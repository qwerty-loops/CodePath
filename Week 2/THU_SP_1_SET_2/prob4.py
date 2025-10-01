#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'roman_to_integer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# from collections import Counter
def roman_to_integer(s):
    # Write your code here
    sum=0
    roman_num={}
    for i,v in enumerate(s):
        if v not in roman_num and v=='I':
            roman_num[v] = 1
        elif v in roman_num and v=='I':
            roman_num[v] += 1
        elif v not in roman_num and v=='V':
            roman_num[v] = 5
        elif v in roman_num and v=='V':
            roman_num[v] += 5
        elif v not in roman_num and v=='X':
            roman_num[v] = 10
        elif v in roman_num and v=='X':
            roman_num[v] += 10
        elif v not in roman_num and v=='L':
            roman_num[v] = 50
        elif v in roman_num and v=='L':
            roman_num[v] += 50
        elif v not in roman_num and v=='C':
            roman_num[v] = 100
        elif v in roman_num and v=='C':
            roman_num[v] += 100
        elif v not in roman_num and v=='D':
            roman_num[v] = 500
        elif v in roman_num and v=='D':
            roman_num[v] += 500
        elif v not in roman_num and v=='M':
            roman_num[v] = 1000
        elif v in roman_num and v=='M':
            roman_num[v] += 1000
        elif v in roman_num and v=='I' and s[i+1] =='X':
            roman_num[v] += 9

    
    for i in roman_num.values():
        sum+=i
    return sum
    # num=0
    # for i in range(len(s)):
        
    #     if s[i]=='V':
    #         num+=5
    #     elif s[i]=='L':
    #         num+=50
    #     elif s[i]=='D':
    #         num+=500
    #     elif s[i]=='M':
    #         num+=1000
    #     elif s[i]=='I' and s[i+1] =='V':
    #         num+=4
    #     elif s[i]=='I' and s[i+1]=='X':
    #         num+=9
    #     elif s[i]=='I':
    #         num+=1
    #     elif s[i]=='X' and  s[i+1]=='L':
    #         num+=50
    #     elif s[i]=='X' and s[i+1] =='C':
    #         num+=90
    #     elif s[i]=='X':
    #         num+=10
    #     elif s[i]=='C' and s[i+1] =='D':
    #         num+=400
    #     elif s[i]=='C' and s[i+1] =='M':
    #         num+=900
    #     elif s[i]=='C':
    #         num+=100
    # return num
roman_string = "IX"
result = roman_to_integer(roman_string)
print(result)
