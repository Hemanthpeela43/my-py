def mergesort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        mergesort(left_array)
        mergesort(right_array)
        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j +=1
            k += 1
        while i < len(left_array):
                arr[k] =left_array[i]
                i += 1
                k += 1
        while j < len(right_array):
            arr[k] =right_array[j]
            j += 1
            k += 1
def printr(arr):
    for i in range (len(arr)):
        print(arr[i],end= " ")
if __name__ == '__main__':
    arr = [12, 5, 43, 26, 754, 2, 1, 56, 78, 54]
    print("before sorting the arry is : ")
    printr(arr)
    mergesort(arr)
    print()
    print("after  sorting the arry is : ")
    printr(arr)
