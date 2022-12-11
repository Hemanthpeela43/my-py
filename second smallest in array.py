import math


def second_small(arr):
    sml=arr[0]
    for i in range (1,len(arr)):
        if arr[i]<sml:
            sml=arr[i]
        ssm=math.inf
    for i in range (0,len(arr)):
        if sml != arr[i] and arr[i] < ssm:
            ssm=arr[i]
    return ssm
arr=[2,1,-2,34,-8,56,-8]
#arr.sort()
print(second_small(arr))
#only applicable for unique elements only
