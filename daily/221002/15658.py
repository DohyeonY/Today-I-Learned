N = int(input())
lst = list(map(int, input().split()))
cnt = list(map(int, input().split()))
maxresult = -999999999999999999
minresult = 999999999999999999

def dfs(a, r) :
    global maxresult
    global minresult
    if a == N :
        maxresult = max(maxresult, r)
        minresult = min(minresult, r)
        return
    
    if cnt[0] > 0 :
        cnt[0] -= 1
        dfs(a + 1, r + lst[a])
        cnt[0] += 1

    if cnt[1] > 0 :
        cnt[1] -= 1
        dfs(a + 1, r - lst[a])
        cnt[1] += 1

    if cnt[2] > 0 :
        cnt[2] -= 1
        dfs(a + 1, r * lst[a])
        cnt[2] += 1

    if cnt[3] > 0 :
        cnt[3] -= 1
        dfs(a + 1, int(r / lst[a]))
        cnt[3] += 1

dfs(1, lst[0])
print(maxresult)
print(minresult)