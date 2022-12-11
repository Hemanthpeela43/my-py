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
