a=int(input("entert a nmuber to : "))
n1=0
n2=1
print("Fibonacci series of given number {} is {} {} ".format(a,n1,n2),end=" ")
for i in range (2,a):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")



print()
print()

#using Recursive function
def fibonacciSeries(i):
    if i <= 1:
        return i
    else:
        #important logic 
        return (fibonacciSeries(i-1)+fibonacciSeries(i-2))

if a <= 0 :
    print("enter a positive nmuber ")
else:
    print("Fibonacci series of given number ",end=" ")
    for i in range (a):
        print(fibonacciSeries(i), end=" ")
