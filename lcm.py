a=int(input("enter a number : "))
b=int(input("enter another number : "))
maxi=max(a,b)
li=a*b
for i in range(maxi,li+1,maxi):
    if i%a ==0 and i % b==0:
        lcm=i
        break
print("the lcm of the given two numbers is : ",lcm)

print()
def lcmfinder(a,b):
    if a>b:
        maxi=a
    else:
        maxi=b
    temp=maxi
    while True:
        if maxi%a==0 and maxi%b==0:
            hcf=maxi
            break
        maxi=maxi+temp
    print("the lcm of given two numbers is : ",maxi)
lcmfinder(a,b)
