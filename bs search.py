def rbs(arr,left,right,target):
    if right >= left:
        while (left <=right):
            m=left+right//2
            if arr[m] == target:
                return m
            if arr[m] > target:
                right=m-1
            else:
                left=m-1




def bs(arr,left ,right,target):
    if right >=left:
        m=right+left//2
        if arr[m]==target:
            return m
        if arr[m] > target:
            return bs(arr,left,m-1,target)
        else:
            return bs(arr,m-1,right,target)

arr=[3,5,7,9,12,15,16,18,19,22]
target=int(input("enter a number  to find : "))
if target not in arr:
    target=int(input("pls enter a number that is in the arr"))
l=len(arr)
res=rbs(arr,0,l-1,target)

if res==-1:
    print("the item is not found")
else:
    print("the is found at index :",res)

print()


ress=bs(arr,0,l-1,target)
if ress==-1:
    print("recurrion the item is not found")
else:
    print("recurrion the item is found at index :",ress)
