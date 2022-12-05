#strong number
a=int(input("enter a number : "))
b=a
num=0
while a !=0:
    rem=a%10
    mul=1
    for i in range (1,rem+1):
        mul=mul*i
    a=a//10
    num=num+mul
if num==b:
    print("the number is strong number ")
else:
    print("the number is not strong number ")

#using recurssive function
def check(c,numb):
   if c==0:
       return numb
   if c !=0:
       nu=1
       rem=c%10
       for i in range (1,rem+1):
           nu=nu*i
       numb=numb+nu
       return check(c//10 ,numb)


c=b
numb=0
if (check(c,numb)==b):
    print("the number is strong number ")
else:
    print("ther number is not strong number ")
