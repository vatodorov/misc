# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 10:55:12 2017

@author: Valentin.Todorov
"""

#!/bin/python
import sys
import os

# Complete the function below.
def  sumOfIntegers(arr):
    return sum(arr)

f = open(os.environ['OUTPUT_PATH'], 'w')

_arr_cnt = int(raw_input())
_arr_i = 0
_arr = []

while _arr_i < _arr_cnt:
    _arr_item = int(raw_input());
    _arr.append(_arr_item)
    _arr_i += 1

res = sumOfIntegers(_arr);
f.write(str(res) + "\n")

f.close()


# This is a test
a = 5 + 2
print a