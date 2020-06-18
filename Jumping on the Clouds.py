#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    step = 1
    ctr = [0, 0]
    i = 0
    if (len(c) == 2):
        return 1
    while (i < len(c) - 1):
        i += step
        if (c[i] == 1):
            i += step
            ctr[0] += 1
        else:
            ctr[0] += 1
    step = 2
    i = 0
    while (i < len(c) - 2):
        i += step
        if i == len(c) - 2:
            i += 1
            ctr[1] += 1
        if (c[i] == 1):
            i -= 1
            ctr[1] += 1
        else:
            ctr[1] += 1
    return (min(ctr))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
