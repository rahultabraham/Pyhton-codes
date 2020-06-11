#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    if (len(s)) == 1:
        return "YES"
    dic = {}
    for i in s:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    ele = dic[s[1]]
    arr = []
    for value in dic.values():
        arr.append(value)
    ele = arr[0]
    ctr = 0
    j = 0
    ctr2 = 0

    for index, element in enumerate(arr):
        if ele != element:
            ctr += 1
            j = index
    if ctr == 0:
        return ("YES")
    elif ctr == 1:
        diff = abs(ele - arr[j])
        if (diff == 1):
            return ("YES")
        else:
            for value in arr:
                if value == 1:
                    ctr2 += 1
            if (ctr2 == 1):
                return 'YES'
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
