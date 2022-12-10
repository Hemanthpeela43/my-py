# write a progeam that converts hexa into decimal


def convert(hexa):
    decimal=0
    pos=0
    length=len(hexa)
    for i in range (length-1,-1,-1):
        if hexa[i] >= '0' and hexa[i] <= '9':
            digit=ord(hexa[i])-48
            decimal=decimal+digit*pow(16,pos)
            pos=pos+1

        elif hexa[i] >= 'A' and hexa[i] <= 'Z':
            digit=ord(hexa[i])-65
            decimal=decimal+digit*pow(16,pos)
            pos=pos+1
        else:
            return "the number is not a hexa decimal number "
    return decimal
hexa=input("enter a hexa decimal number : ")
print("The decimal value of given number is : ",convert(hexa))
