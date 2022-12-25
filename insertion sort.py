def insertion(arr,l):
    for i in range (1,l):
        temp=arr[i]
        j=i-1
        while (j >=0 and temp < arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
    return arr

arr=[300,15,7,19,1002,1115,16,18,19,22]
l=len(arr)

print("before sorting the array is : ",arr)
insertion(arr,l)
print("after sorting the array is : ",arr)
