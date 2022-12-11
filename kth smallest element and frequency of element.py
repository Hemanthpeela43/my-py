arr=[1,3,2,1,4,2,5,6,3,3,4]
arr.sort()
print(arr)
n=len(arr)
k=4
i=0
while i<n:
    while i < n-1and arr[i] == arr[i+1]:
        i=i+1
    k=k-1
    if k==0:
        break
    i=i+1
print(arr[i])
print()

ar=[1,2,3,1,4,5,2,1,3,4,6,7,8,7,6,5,6,7,5]
ar.sort()
print(ar)
n=len(ar)
i=0
while i <n:
    cnt=0
    while i <n-1and ar[i]==ar[i+1]:
        cnt=cnt+1
        i=i+1
    print((ar[i],cnt+1))
    i=i+1
