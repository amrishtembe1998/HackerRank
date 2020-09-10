#!/bin/python3

import math
import os
import random
import re
import sys
from array import *
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    Lsum = 0
    i,j = 0,0
    while(i < len(arr)):
        Lsum = Lsum + arr[i][j]
        i = i + 1
        j = j + 1
    Rsum = 0
    i,j = 0,len(arr)-1
    while(i < len(arr)):
        Rsum = Rsum + arr[i][j]
        i = i + 1
        j = j - 1   
    return abs(Lsum - Rsum)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
