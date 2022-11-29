def findrev (number,reve):
    if number==0:
        return reve
    remainder = int(number%10)
    reve=(reve*10) +remainder
    return findrev(int(num/10),reve)

number = 12345
#print("the number is ",number)
reve=0
print(findrev(number,reve))
