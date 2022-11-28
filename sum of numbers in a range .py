#summ of n numbers in a given range


#1using loop

a,b=3,6
sum=0
for i in range (a,b+1):
    sum=sum+i

print("the sum of numbers in a given range is {} ".format(sum))

# method 2 using formula
sum=((b*(b+1)/2)-(a*(a+1)/2) +a)
print("the sum of numbers in a given range by formula  is {} ".format(sum))
#method 3 using receussive function

def add(a,b,s):
    if a>b:
        return s
    return a+add(a+1,b,s)

s=0
print( " the sum of given numbers by in range by using recurrison is ",add(a,b,s))


