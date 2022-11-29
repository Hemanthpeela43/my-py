a= int(input("enter a nmuber to reverse "))

num=a
rev=0
while num!=0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
print("1 reverse of given number is {}".format(rev))


#string slicing
num1=a
print("2 reverse of given nmuber is ",str(num1)[::-1])

#using recurssion
def findrev (number,reve):
    if number==0:
        return reve
    remainder = int(number%10)
    reve=(reve*10) +remainder
    return findrev(int(number/10),reve)

number = 12345
#print("the number is ",number)
reve=0
print(findrev(number,reve))
