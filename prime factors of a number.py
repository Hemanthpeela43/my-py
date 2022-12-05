#finding prime factors of a number


#using simple iteration
a=int(input("enter a number : "))
arr=[]
for i in range (2,a+1):
    flag=0
    if a%i==0:
        for j in range (2,i):
            if i%j==0:
                flag=1
        if flag==0:
            arr.append(i)
print(arr)
print()
#using function
def findp(a,brr):
    for i in range(2, a + 1):
        flag = 0
        if a % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    flag = 1
            if flag == 0:
                 print(i)
brr=[]
findp(a,brr)
