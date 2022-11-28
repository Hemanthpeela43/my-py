#greatest of given two numbers

a,b=12,34

if a>b:
    print(" the greaesr number is {}".format(a))
elif b>a:
    print("the greatest number is {}".format(b))
else:
    print("both numbers are equal ")

print("max of given two numbers is ",max(a,b))

print()
print(a if a>b else b)