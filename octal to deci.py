#converting octal to decimal number :
def convert(num):
    i=0
    deci=0
    while num!=0:
        digi=num%10
        #logic of code
        deci=deci+digi*pow(8,i)
        num=num//10
        i=i+1
    return deci
num=int(input("enter a number : "))
print(convert(num))
