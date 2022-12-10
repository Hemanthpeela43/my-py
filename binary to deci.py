#converting binary to decimal number :
def convert(num):
    i=0
    deci=0
    while num!=0:
        digi=num%10
        deci=deci+digi*pow(2,i)
        num=num//10
        i=i+1
    return deci
num=int(input("enter a number : "))
print(convert(num))
