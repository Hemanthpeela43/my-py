def bs(a,it,l,r):
 if l>=r:
  mid=l+(r-l)//2
  if a[mid]==it:
   return mid
  elif a[mid]>it:
   return bs(a,it,l,r-1)
  else:
   return bs(a,it,l+1,r)
 else:
  return -1

 pass
a=[1,4,5,67,34,23,789,102,334,56]

#[1, 4, 5, 23, 34, 56, 67, 102, 334, 789]
a.sort()
print(a)
item=int(input("enter a number to search : "))

res=bs(a,item,r=0,l=len(a))
if res==-1:
 print("item bot found ")
else :
 print("found at index : ",res)
