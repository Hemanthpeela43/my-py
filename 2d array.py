row = int(input("enter the number of rows :"))
col=int(input("enter the number of columns :"))

martrix=[]

print("the entires are ")
for i in range (row):
    a=[]
    for j in range (col):
        a.append(int(input()))
    martrix.append(a)

for i in range (row):
    for j in range (col):
       print(martrix[i][j],end=" ")
    print()
