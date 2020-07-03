#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    i=0
    j=0
    k=0
    n=len(a)
    temp=0
    while i<n-1:
        j=0
        while j<n-i-1:
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                k+=1
            j+=1
        i+=1
    k=str(k)
    a[0]=str(a[0])
    a[n-1]=str(a[n-1])
    print ("Array is sorted in "+k+" swaps.")
    print("First Element: "+a[0])
    print("Last Element: "+a[n-1])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
