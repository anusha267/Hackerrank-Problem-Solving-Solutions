#!/bin/python3

import math
import os
import random
import re
import sys
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices.sort()
    x=0
    s=0
    i=0
    while i<len(prices):
        if (s+prices[i])<k:
            s+=prices[i]
            x+=1
            
        else:
            break
        i+=1
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
