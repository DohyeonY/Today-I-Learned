import sys
sys.stdin=open("퀵정렬.txt", "r")

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

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))
    quick_s(0, len(arr)-1)
    print(f'#{tc} {arr[N//2]}')