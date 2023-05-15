def f(n):
    if n <=1:
        return n
    else:
        return f(n-1)+f(n-2)
n=int(input("enter a nubmer : "))
print("the fib of number is {}".format(f(n)))