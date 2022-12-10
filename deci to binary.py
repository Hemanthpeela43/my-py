def con(num):
    binary=[]

    while num !=0:
        rem=num%2
        binary.insert(0,rem)
        num=num//2
    return print(''.join(str(x) for x in binary ))

def convert(num):
     binary=0
     i=1

     while num !=0:
         rem=num%2
         num=num//2
         binary=binary + rem*i
         i=i*10
     return binary


num=int(input("enter a number : "))
con(num)
print("binary form of guiven number is : ",convert(num))
