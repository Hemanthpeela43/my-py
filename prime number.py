# prim number program
#normal process
num=int(input("enter a number to check whether it is a prime nuymbewr or not : "))
count=0
for i in range (1,num+1):
    if num%i==0:
        count=count+1
if count==2:
    print("entered number is a prime nmuber ")
else:
    print("not a prime nmuber")

print()
#method tw0
flag=0
for i in range (2,num):
    if num%i==0:
        flag=flag+1
        break
if flag==0:
    print("the given number is prime ")
else:
    print("the given number is not a prime number ")


print()
#method 3
flag=0
for i in range (2,int(num/2+1)):
    if num%i==0:
        flag=flag+1
        break
if flag==0:
    print("the given number is prime ")
else:
    print("the given number is not a prime number ")

print()
#method four
flag=0
for i in range (2,int(pow(num,0.5)+1)):
    if num%i==0:
        flag=flag+1
        break
if flag==0:
    print("the given number is prime ")
else:
    print("the given number is not a prime number ")

#method 5 recrussion

def checkprime (num ,iter=2):
    if num==iter:
        return True
    if num % iter == 0:
        return False
    if num < 2:
        return False
    return checkprime(num ,iter+1)


if(checkprime(num))==True:
    print("the given number is prime number ")
else:
    print("the given number is not a prime nmuber ")
