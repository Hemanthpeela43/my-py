def sor(a):
    for i in range (len(a)):
        k=0
        for j in range (len(a)-i-1):
            if a[j] > a[j+1]:
                k+=1
                a[j],a[j+1]=a[j+1],a[j]
        if k==0:
            break
    return a
def dis(a):
    print(" ".join(str(x) for x in a))
a=[1,4,2,3,4,5]

print("before sorting ")
dis(a)
rs=sor(a)
print("after sorting ")
dis(rs)
