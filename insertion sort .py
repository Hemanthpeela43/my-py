def sor(a):
    for i in range (1,len(a)):
        temp=a[i] # here we are assing the value of which we are cosidering to insert
        j=i-1 #for getting the previous elemets
        while j >=0 and temp < a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
    return a
def dis(a):
    print(" ".join(str(x) for x in a))

# inserion sort
a=[22,1,3,412,34,26,78,2,3,567,49,5]

print("before sorting ")
dis(a)
rs=sor(a)
print("after sorting ")
dis(rs)



