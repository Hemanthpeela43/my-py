#using recurrision
def rls(arr,l,target):
        if arr[l]==target:
            return l
        elif l==-1:
            return -1
        return rls(arr,l-1, target)


def ls(arr,l,target):
    for i in range (l):
        if arr[i]==target:
            return i
    return -1
arr=[10,2,8,20,40,15,25]
target=int(input("enter a number  to find : "))
if target not in arr:
    target=int(input("pls enter a number that is in the arr"))
l=len(arr)
res=ls(arr,l,target)

if res==-1:
    print("the item is not found")
else:
    print("the is found at index :",res)

print("this is obtained using recuerrision ")
ress=rls(arr,l-1,target)
if ress==-1:
    print("recurrion the item is not found")
else:
    print("recurrion the item is found at index :",ress)
