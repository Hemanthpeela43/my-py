#smallest element in a element 
def smallest(arr):
    min=arr[0]
    for i in range (1,len(arr)):
        if arr[i] < min:
            min=arr[i]
    return min
arr=[100,45,32,-67,54,67]
print("the smallest elememt if the given array is : ",smallest(arr))
arr.sort()
print("the smallest elememt if the given array is : ",arr[0])


#linear search 
a=int(input("enter a number to search : "))
n = len(arr)
b = 0
for i in range(0,n):
    if a == arr[i]:
        print("the element {} is in the given element ".format(a))
        b=b+1
        break
if b==0:
    print("the element {}  is not in the arr : ".format(a))
