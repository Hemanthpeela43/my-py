def convert (num):
    hexa=[]
    i=0
    while num !=0:
        rem=0
        rem=num%16
        if rem < 10:
            hexa.insert(0,chr(rem+48))
        else:
            hexa.insert(0, chr(rem +55))
        num=num//16
    print(''.join(str(x) for x in hexa))

num=892
convert(num)
