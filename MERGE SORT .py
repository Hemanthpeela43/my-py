#consists of three 1) input 2) divide 3) merge
def mergesort(list1):#mainlist left list and right list are passing to this
    if len(list1)>1: #base or stopping comdition for recrusion
        mid = len(list1) // 2
        left_list = list1[:mid]
        right_list = list1[mid:]
        #dividing
        mergesort(left_list)  # again again we are calling this
        mergesort(right_list)  # we must use base case to  stop

        #merging
        #left list of index as i and right list of index as j k as list1 index

        i=0
        j=0
        k=0
    #i and j are indexes and always smaller than lists
        while i< len(left_list) and j <len(right_list):
            if left_list[i] < right_list[j]:
                list1[k] = left_list[i]
                i=i+1
                k=k+1
            else:


                list1[k] = right_list[j]
                j=j+1
                k=k+1
        #values left in left index
        while i < len(left_list):
                list1[k] = left_list[i]
                i=i+1
                k=k+1
        while j < len(right_list):
            list1[k] = right_list[j]
            j = j + 1
            k = k + 1
    #return list1

    #input
num=int(input("enter thne number elements in the list : "))
list1=[int(input()) for x in range (num)]
mergesort(list1)
print("the sorted list is : ",list1)
    
