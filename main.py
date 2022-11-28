a,b,c=10,9,23
if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
else:
    max=c
print("maximum of given three numbers is {}".format(max))