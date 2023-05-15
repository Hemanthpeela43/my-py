def sockMerchant(n, ar):
    ar.sort()
    cnt = 0
    i = 0
    while i < n:
        if i < len(ar) - 2:
            if ar[i] == ar[i + 1]:
                cnt += 1
                i = i + 2
        else:
            i = i + 1
    return cnt


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)

   # fptr.write(str(result) + '\n')

    #fptr.close()
