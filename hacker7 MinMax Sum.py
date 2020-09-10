L = [1,2,3,4,5]
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    min = 0
    for i in arr[0:len(arr)-1]:
        min = min + i
    max=0
    for i in arr[1:len(arr)]:
        max = max + i
    print(min,max)
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
