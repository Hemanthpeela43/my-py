a=int(input("enter a number to check amstrong or not : "))

num=a
rev=0
while(num!=0):
    rem=int(num%10)
    rev=rev+pow(rem,3)
    num=num/10
print(rev)
if rev==a:
    print("the given number is armstrong number ")
else:
    print("the given number is not a armstrong number")

print()
#using for loop

num1=a
reve=0
for i in range(len(str(num1))):
    rem=int(num1%10)
    reve=reve+pow(rem,3)
    num1=int(num1/10)
print(reve)
if reve==a:
    print("the number is a armstrong number ")
else:
    print("the number is not a armstrong number ")

print()
#using recurrisive function
def ch(num2,re):
    if num2==0:
        return re
    rem=int(num2%10)
    re=re+pow(rem,3)
    return ch((num2/10),re)
num2=a
re=0
ree=ch(num2,re)
print(ree)
if ree==a:
    print("the given number is a arnstrong number ")
else:
    print("the given number is not a  armstrong number")
