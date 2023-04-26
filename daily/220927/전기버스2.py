import sys
sys.stdin=open("전기버스2.txt", "r")

def dfs(idx, s):
    global result
    if s >= result :
        return
    if idx >= N - 1 :
        if s <= result :
            result = s
        return
    for i in range(arr[idx]):
        dfs(idx+i+1, s + 1)


T = int(input())

for tc in range(1, T+1) :
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    result = 9999999999
    dfs(0, -1)

    print(f'#{tc} {result}')