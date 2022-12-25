def maxArea(arr, length):
    res=0
    for i in range (length):
        cnt=1
        for j in range (i-1,-1,-1):
            if arr[j]>=arr[i]:
                cnt+=1
            else:
                break
        for z in range (i+1,length):
            if arr[z]>=arr[i]:
                cnt+=1
            else:
                break
        temp=arr[i]*cnt
        res=max(res,temp)
    return res


arr = [12, 3, 4, 4, 1, 5, 7]
print("Max Area: ", maxArea(arr,len(arr)))
