a=int(input("enter a number "))
b=a
sum=0
for i in range (1,a):
    if a % i==0:
        sum=sum+i
if sum==a:
    print("the number is perfect number ")
else:
    print("the number is not perfect number ")

print()



sum_n=0
def perfectss(a,i):
    global sum_n
    if i<=a//2:
        if a % i == 0:
            sum_n=sum_n+i
        i=i+1
        perfectss(a, i)
    return sum_n


c=b
#if getSumDivisors(num, 1) == num:

if perfectss(c,1) == c:
    print("the number is perfect number ")
else:
    print("the number is not perfect number ")

