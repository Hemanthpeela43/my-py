def bubblesort (arr):
    n=len(arr)
    for i in range (n-1):
        for j in range (n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
def display(arr):
    print(" ".join(str(x) for x in arr))
def bb(arr):
    n=len(arr)
    temp=0
    for i in range (n-1):
        cnt=0
        for j in range (i,n-1):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[j]=arr[i]
                arr[i]=temp
                cnt=True
        if not cnt:
            print()
            print("the array is already sorted : ")
            break

arr=[5,3,1,9,8,2,4,7]
print()
print("before bubble sort ")
display(arr)
bubblesort(arr)
print()
print("after bubble sort ")
display(arr)
print()
print("after bb bubble sort ")
bb(arr)
display(arr)
