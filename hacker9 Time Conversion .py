#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    
    a = s.split(":")
    #print("The value of a is: ",a)
    str1 = str(a[2])
    #print("The value of str is: ",str1)
    x = list(str1)
    #print("value of x is: ",x)
    if(a[0]=="12" and x[2]=="A"):
        return "00"+":"+a[1]+":"+x[0]+x[1]
    elif(a[0]=="12" and x[2]=="P"):
        return a[0]+":"+a[1]+":"+x[0]+x[1]
    elif(x[2]=="P"):

        x1 = int(a[0])+12
    
        #print("value of x1 is : ",x1)
        x2 = str(x1)
        return str(x2)+":"+str(a[1])+":"+x[0]+x[1]
    else:
        return a[0]+":"+a[1]+":"+x[0]+x[1]

    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
