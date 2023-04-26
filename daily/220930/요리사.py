import sys
sys.stdin = open("요리사.txt")

from itertools import combinations


def check(arr, i) :
    cnt = 0
    for a, b in combinations(i, 2) :
        # print(a, b)
        cnt += arr[a][b] + arr[b][a]
    return cnt

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    lst = []
    result = 9999999999999
    for i in range(N) :
        lst.append(i)
    for i in combinations(lst, N//2) :
        # print(i)
        # 다른걸 찾아내는 방법
        another = list(set(range(N)) - set(i))
        # print(another)
        result1 = check(arr, i)
        result2 = check(arr, another)

        if result > abs(result1 - result2) :
            result = abs(result1 - result2)

    print(f'#{tc} {result}')