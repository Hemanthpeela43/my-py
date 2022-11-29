a=int(input("enter a number : "))
num=a
rev=0
while num !=0:
    rem=num%10
    rev=rev*10 +rem
    num=num//10
if rev==a:
    print("the given number is a palindrome number ")
else:
    print("not pallindronme ")

print()


#using recurrisve function
def revof(num1,reve):
    if num1==0:
        return rev
    remi=int(num1%10)
    reve=(reve*10)+remi
    return revof(int(num1/10),reve)
num1=a
reve=0
nun=revof(num1,reve)
if nun==a:
    print("the given number is a palindrome number : ")
else:
    print("the number is not a palindrome : ")
