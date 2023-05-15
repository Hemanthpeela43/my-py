s=int(input("enter the nubmer of rows : "))

for i in range (s):
    for j in range (0,s-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("x",end=" ")
    print()
