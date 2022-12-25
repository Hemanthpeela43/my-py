from collections import deque
def stockspan(a):
    s=deque()
    s.append(0)
    print(1,end=" ")
    #1 0 1 2 3 4 5 6 7 8 9 10 11
    for i in range (1,len(a)):
        while len(s)!=0 and a[s[-1]] <= a[i]:
            s.pop()
        if len(s)==0:
            print(i+1,end=" ")
        else:
            print(i-s[-1],end=" ")
        s.append(i)

a=[100,20,30,60,38,36,32,55,80,50,120]
stockspan(a)
