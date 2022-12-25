def stockspan(a):
    l=len(a)
    for i in range (l):
        cur=1
        j=i-1
        while j >= 0 and a[j] <= a[i]:
            cur+=1
            j-=1
        print(cur,end=" ")
a=[12,14,15,17,5,12,10,13,20]
stockspan(a)
