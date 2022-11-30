#factors of a number


a=int(input("enter a number "))
print("factors of given number is : ",end=" ")
for i in range (1,a+1):
    if a%i==0:
        print(i,end=" ")
