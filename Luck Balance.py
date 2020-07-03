
import math
import os
import random
import re
import sys

def luckBalance(k, contests):
    i=0
    s=0
    l=[]
    while i<len(contests):
        if (i%2!=0 and contests[i]==1) or (i==0 and contests[i]==1):
            l.append(contests[i-1])
        if contests[i]==0 and i%2!=0:
            s+=contests[i-1]
        i+=1
    l.sort(reverse=True)
    i=0
    while i<k and i<len(l):
        s=s+l[i]
        i+=1
    while i<len(l):
        s=s-l[i]
        i+=1
    return s
        
n,k=list(map(int, input().split()))
i=0
contests=[]
while i<n:
    x,y=map(int,input().split())
    contests.append(x)
    contests.append(y)
    i+=1
print(luckBalance(k,contests))
    
