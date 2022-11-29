a=int(input("enter lowest number : "))
b=int(input("enter highest number : "))
primes=[2]
for i in range(a,b+1):
    flag = 0
    if i < 2:
        flag = 1
    if i % 2 == 0:
        continue
    iter = 2
    while iter < int(i/2):
        if i % iter ==0:
           flag = 1
           break
        iter += 1
    if flag == 0:
        primes.append(i)
print(primes)
