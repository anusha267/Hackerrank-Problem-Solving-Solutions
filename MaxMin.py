import os

def maxMin(k, arr):
    arr.sort()
    a=[]
    i=0
    while i<(len(arr)-k+1):
        j=i+k-1
        a.append((arr[j]-arr[i]))
        i+=1
    return min(a)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    k = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
