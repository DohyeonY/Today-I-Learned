N, M = map(int, input().split())
lst = []

def dfs(a, idx) :
    if a - 1 == M :
        print(' '.join(map(str, lst)))
        return
    
    for i in range(idx, N+1) :
        lst.append(i)
        dfs(a+1, i)
        lst.pop()

dfs(1,1)