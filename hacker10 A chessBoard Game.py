#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chessboardGame function below.
def chessboardGame(x, y):
    x1= x % 4
    y1= y % 4
    if(x1==0 or x1==3 or y1==0 or y1==3):
        return "First"
    else:
        return "Second"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        xy = input().split()

        x = int(xy[0])

        y = int(xy[1])

        result = chessboardGame(x, y)

        fptr.write(result + '\n')

    fptr.close()
