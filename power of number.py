#power of a nmuber

num=int(input("enter a number : "))
power=int(input("enter power value : "))
print("power of a given number is ",pow(num,power))
print()

#using iteration
p=1
for i in range (power):
    p=num*p
print("power of a given number is ",p)

#usingpython operator
print()
print("power of a given number is ",num**power)

print()


#using recrussive function

def p(num,power):
    if power==0:
        return 1
    return num* p(num,power-1)
print("power of a given number is ",p(num,power))
