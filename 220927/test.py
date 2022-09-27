def partition(L, R) :
    p = L
    i = L + 1
    j = R

    while i <= j :
        while i <= j and arr[i] <= arr[p] :
            i += 1
        while i <= j and arr[j] > arr[p] :
            j -= 1
        if i < j :
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]
    return j

def quick_s(L, R) :
    if L < R :
        p = partition(L, R)
        quick_s(L, p-1)
        quick_s(p+1, R)
        # print(arr)

arr = [3, 2, 4, 6, 9, 8, 1, 5, 7]
quick_s(0, len(arr)-1)
print(arr)
