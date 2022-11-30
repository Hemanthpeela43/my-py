#factorial of a number
# simple iteration
a=int(input("enter a number : "))
b=1
for i in range (1,a+1):
    b=b*i
print("factorial of a  given number is ",b)

print()

#using function
def factorialof(c,a):
    for i in range (c,a+1):
        c=c*i
    return c
c=1
d=factorialof(c,a)
print("factorial of given number is : ",d)

print()
#using recurssive function
def getfact(a):
    if a==0:
        return 1
    return a*getfact(a-1)

fact=getfact(a)
print("factorial of given number is ",fact)
