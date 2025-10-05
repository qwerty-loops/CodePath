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
    roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    i=0
    roman_sum=0
    while i<len(s):
        if s[i] in roman_dict:
            if (i+1)<len(s) and s[i]=="I" and s[i+1]=="V":
                roman_sum+=4
                i+=2
            elif (i+1)<len(s) and s[i]=="I" and s[i+1]=="X":
                roman_sum+=9
                i+=2
            elif (i+1)<len(s) and s[i]=="X" and s[i+1]=="L":
                roman_sum+=40
                i+=2
            elif (i+1)<len(s) and s[i]=="X" and s[i+1]=="C":
                roman_sum+=90
                i+=2
            elif (i+1)<len(s) and s[i]=="C" and s[i+1]=="D":
                roman_sum+=400
                i+=2
            elif (i+1)<len(s) and s[i]=="C" and s[i+1]=="M":
                roman_sum+=900
                i+=2
            else:
                roman_sum+=roman_dict[s[i]]
                i+=1
                # roman_sum+=roman_dict.get(s[i])
    return roman_sum


roman_string = "IV"
result = roman_to_integer(roman_string)
print(result)
