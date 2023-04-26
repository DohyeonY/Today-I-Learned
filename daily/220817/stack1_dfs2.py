def dfs(v) :        # 재귀
    print(v)        # v 방문
    visited[v] = 1
    for w in adjlist[v] :
        if visited[w]  == 0 :
            dfs(w)




V, E = map(int, input().split())
N = V + 1
adjlist = [[] for _ in range(N)]
for _ in range(E) :
    a, b = map(int, input().split())
    adjlist[a].append(b)
    adjlist[b].append(a)

visited = [0] * N   # visited 생성
dfs(0)
print()