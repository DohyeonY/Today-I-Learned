def dfs_r(v) :
    visited[v] = True
    for w in G[v] :
        if not visited[w] :
            dfs_r(w)

def dfs(s) :
    Q = []
    visited = [False] * (N+1)
    Q.append(s)
    visited[s] = True
    while Q :
        v = Q.pop()
        print(v)
        # visited[v] = True
        for w in G[v] :
            if not visited[w] :
                Q.append(w)
                visited[w] = True

def bfs(v) :
    Q = []
    visited = [False] * (N+1)
    Q.append(v)
    visited[v] = True
    while Q :
        v = Q.pop(0)
        print(v)
        for w in G[v] :
            if not visited[w] :
                Q.append(w)
                visited[v] = True

lst = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7
G = [[] for _ in range(N+1)]
for i in range(0, len(lst), 2) :
    n1 = lst[i]
    n2 = lst[i+1]
    G[n1].append(n2)
    G[n2].append(n1)
print(G)

# G = [[0] * (N+1) for _ in range(N+1)]
# for i in range(0, len(lst), 2) :
#     n1 = lst[i]
#     n2 = lst[i + 1]
#     G[n1][n2] = 1
#     G[n2][n1] = 1
# print(G)
bfs(1)