def partition(L, R) :
    p = R
    i = L - 1
    for j in range(L, R) :
        if arr[j] < arr[p] :
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    i += 1
    arr[p], arr[i] = arr[i], arr[p]
    return i



def quick_s(L, R) :
    if L < R :
        p = partition(L, R)
        quick_s(L, p-1)
        quick_s(p+1, R)
        # print(arr)

arr = [3, 2, 4, 6, 9, 8, 1, 5, 7]
quick_s(0, len(arr)-1)
print(arr)