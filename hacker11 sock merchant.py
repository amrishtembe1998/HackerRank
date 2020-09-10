#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    count = []
    result = []
    pairs = 0
    for i in ar:
        count.append(ar.count(i))
    #print(count)
    res = dict(zip(ar,count))
    #print(res)
    for values in res:
        res[values] = res[values]//2
        pairs = pairs + res[values]
    #print(res)
    return pairs
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()




    
