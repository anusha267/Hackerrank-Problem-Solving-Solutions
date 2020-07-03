#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    sum=[]
    i=2
    sum=[0]*n
    sum[0]=arr[0]
    sum[1]=max(arr[1],sum[0])
    while i<len(arr):
        sum[i]=max(arr[i],sum[i-1],(arr[i]+sum[i-2]))
        i+=1
    return sum[-1]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
