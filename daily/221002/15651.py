N, M = map(int, input().split())
lst = []

def dfs(a) :
    if a - 1 == M :
        print(' '.join(map(str,lst)))
        return
    
    for i in range(1, N+1) :
        lst.append(i)
        dfs(a+1)
        lst.pop()
dfs(1)

