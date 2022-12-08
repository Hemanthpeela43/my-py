#method 1
from math import sqrt
n=int(input("enter a number : "))
sq=int(sqrt(n))
print(sq)
if sq*sq==n:
    print("yes")
else:
    print("no")

#using function

def issq(n):
    if n >=0:
        sq=int(sqrt(n))
        return sq*sq == n
    return False

if issq(n):
    print("true")
else:
    print("false ")
