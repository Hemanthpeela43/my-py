#counting distinct elements :
arr=[30,50,30,10,20,40,10,20]
n=len(arr)
visted=[False]*n
cnt=0
for i in range (n):
    if not visted[i]:
        for j in range (i+1,n):
            if arr[i]==arr[j]:
                visted[j]=True
        cnt=cnt+1
print("the no of distinct elements in the array is ",cnt)
print()

#method 2 sorting the array is going to reduce the space complixity
def countt(arr,n):
    arr.sort()
    cnt = 0
    i = 0
    while i < n:
        while i < n-1 and arr[i] == arr[i + 1]:
            i = i + 1
        cnt = cnt + 1
        i = i + 1
    return cnt

arr=[5,8,5,7,10,5,8]
#arr.sort()
n=len(arr)
print("the no of distinct elements in the array is : ",countt(arr,n))
print()
#method 3
def countt(arr,n):
    cnt=0
    for i in range (0,n):
        flag=False
        for j in range (i+1,n):
            if arr[i]==arr[j]:
                flag=True
        if flag == False:
            cnt=cnt+1
    return cnt

arr=[5,8,5,7,10,5,8]
n=len(arr)
print("the no of distinct elements in the array is : ",countt(arr,n))
