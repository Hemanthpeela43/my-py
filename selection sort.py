def selection(arr,l):
    for i in range (l):
        small=i
        for j in range (i+1,l):
            if arr[small]>arr[j]:
                small=j
        arr[i],arr[small]=arr[small],arr[i]
    return arr
arr=[300,15,7,19,1002,1115,16,18,19,22]
l=len(arr)
print("before sorting the array is : ",arr)
selection(arr,l)
print()
print("after sorting the array is : ",arr)
