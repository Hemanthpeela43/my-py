#printing previous greather number  using stack :
#time = o(n)^2


#normal code
def stockspan(a):
    for i in range (len(a)):
        flag=0
        #a=[12,10,20,22,15,14,18,32,20,22,19]
        for j in range(i-1,0,-1):
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

#optimal code using stacks
#time = o(n)

def sstockspan(a):
    s=[]
    s.append(a[0])
    print("-",end=" ")
    for i in range (1,len(a)):
        while len(s)!=0 and s[-1] <= a[i]:
            s.pop()
        if len(s)==0:
            print("-",end=" ")
        else:
            print(s[-1],end=" ")
        s.append(a[i])

#drive code 
a=[12,20,22,15,14,18,32,20,22,19]
print()
sstockspan(a)
a=[30,50,20,15,25]
print()
sstockspan(a)
