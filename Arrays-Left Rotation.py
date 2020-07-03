
inp=list(map(int,input().split()))
a=list(map(str,input().split()))
i=0
if inp[0]<inp[1]:
    inp[1]=inp[1]%inp[0]
a=a[inp[1]:]+a[:(inp[1])]
      
i=0
y=" ".join(a)
print(y)
