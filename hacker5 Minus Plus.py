L = [-4,3,0,-9,4,1]
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive, negative, zero = 0,0,0
    for i in arr:
        if(i > 0):
            positive = positive + 1
        elif(i < 0):
            negative = negative + 1
        else:
            zero = zero + 1
    #print(positive,negative,zero)
    a = positive/len(arr)
    b = negative/len(arr)
    c = zero/len(arr)
    print ('%.6f'%a)
    print('%.6f'%b)
    print('%.6f'%c)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
