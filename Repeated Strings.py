#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
   stri=""
   i=0
   k=0
   
   if len(s)>=n:
       while i<n:
           if s[i]=='a':
               k+=1
           i+=1
       return k
   else:
       x=n%len(s)
       n=n-x
       n=n//len(s)
       i=0

       while i<(len(s)):
           if s[i]=='a':
               k+=1
           i+=1
       k=k*n
       i=0
       while i<x:
           if s[i]=='a':
               k+=1
           i+=1

       
       
   return k

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
