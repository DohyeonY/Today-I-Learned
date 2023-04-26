import sys
sys.stdin=open("이진탐색.txt", "r")

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

def binarySearch(N, arr, key) :
    global cnt
    low = 0
    high = N - 1
    flag = 0
    while low <= high :
        mid = (low + high) // 2
        if arr[mid] == key :            # 중앙
            cnt += 1
            return
        if arr[mid] > key :           # 왼쪽
            high = mid - 1
            if flag != 1 :
                flag = 1
            else :
                return
        else :                          # 오른쪽
            low = mid + 1
            if flag != 2 :
                flag = 2
            else :
                return
    return

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    # print(arr)
    # quick_s(0, len(arr)-1)
    # print(arr)
    cnt = 0
    for i in B :
        # print(i)
        binarySearch(N, arr, i)

    print(f'#{tc} {cnt}')