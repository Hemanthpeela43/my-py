#printing next greather number  using stack :
#time = o(n)^2


#normal code
from  collections import  deque
def stockspan(a):
    for i in range (len(a)):
        flag=0
        for j in range (i+1,len(a)):
            if a[j] > a[i]:
                print(a[j],end=" ")
                flag+=1
                break
        if flag==0:
            print("-",end=" ")

#drive code
a=[12,20,22,15,14,18,32,20,22,19]
stockspan(a)
a=[30,50,20,15,25]
print()
stockspan(a)

#optimal solution usibng stacks
def sstockspan(a):
    size=len(a)
    s=deque()
    l=[]
    s.append(a[size-1])
    l.append("-")
    for i in range (size-2,-1,-1):
        while len(s)!=0 and s[-1] <= a[i]:
            s.pop()
        if len(s)==0:
            l.append("-")
        else:
            l.append(s[-1])
        s.append(a[i])
    l.reverse()
    print(" ".join (str(x) for x in l))

print()
a=[12,20,22,15,14,18,32,20,22,19]
sstockspan(a)
a=[30,50,20,15,25]
print()
sstockspan(a)
