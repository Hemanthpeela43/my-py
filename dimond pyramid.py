s=int(input("enter the nubmer of rows : "))

for i in range (0,s+1):
    for j in range (0,s-i):
        print(end=" ")
    for j in range (0,i):
        print("x",end=" ")
    print()

for i in range (s-1,0,-1):
    for j in range(0,s-i):
        print(end=" ")
    for j in range (0,i):
        print("x",end=" ")
    print()
