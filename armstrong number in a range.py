a=10
b=10000
arm=[]
def isarm(i):
    ord = len(str(i))
    rev = 0
    j = i
    while j > 0:
        rem = int(j % 10)
        rev = rev + pow(rem, ord)
        j = int(j / 10)
    if rev == i:
        arm.append(i)
        return arm


print(arm)
for i in range (a,b+1):
   isarm(i)
print(arm)
