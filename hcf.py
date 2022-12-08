a=int(input("enter a number : "))
b=int(input("enter another number : "))
for i in range (1,min(a,b)):
    if a %i==0 and  b%i == 0 :
        hcfa=i
print("hcf if given numbers is ",hcfa)

while (a!=b):
    if a>b:
        a=a-b
    else:
        b=b-a
print("hcf of the givrn numbers is : ",a)
