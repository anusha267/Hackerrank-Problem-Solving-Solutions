#!/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys
def reverse(string): 
    string = string[::-1] 
    return string 
# Complete the substrCount function below.
#def substrCount(n, s):
    x=list(s)
    y=[]
    i=0
    r=0
    while i<len(x):
        j=0
        while j<len(x)+1:
            if i<j:
                y=(s[i:j])
                if len(y)==1:
                    r+=1
                else:
                   if len(y)%2==0 and y[:len(y)//2]==y[len(y)//2:]:
                        r+=1
                   elif (len(y)%2!=0) and (y[:len(y)//2]==y[(len(y)//2)+1:]):
                            r+=1
                   else:
                       continue
            j+=1
        i+=1
    
    
    # # while i<len(y):
    #     w=y[i]
    #     m=list(w)
    #     l=len(w)
    #     l2=l//2
    #     l3=l2
    #     m=list(w)
    #     if len(m)==1:
    #         r+=1
    #     else:
    #         if l%2==0:
    #             if w[:l//2]==w[l//2:]:
    #                 r+=1
    #         else:
    #             if w[:l//2]==w[(l//2)+1:]:
    #                 r+=1
    #     i+=1
    return r
def substrCount(n, s):
    l = []
    count = 0
    cur = None

# 1st pass
    for i in range(n):
        if s[i] == cur:
            count += 1
        else:
            if cur is not None:
                l.append((cur, count))
            cur = s[i]
            count = 1
    l.append((cur, count))

    ans = 0
        
# 2nd pass
    for i in l:
        ans += (i[1] * (i[1] + 1)) // 2

# 3rd pass
    for i in range(1, len(l) - 1):
        if l[i - 1][0] == l[i + 1][0] and l[i][1] == 1:
            ans += min(l[i - 1][1], l[i + 1][1])

    return ans            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
