def dfs(v) :                            # 노말한 dfs
    s = []
    s.append(v)
    visited[v] = True
    while s :
        v = s.pop()
        print(v, end=' ')
        for w in G[v] :
            if not visited[w] :
                s.append(w)
                visited[w] = True




def dfsr(v) :                           # 재귀 이용한 dfs
    visited[v] = True
    print(v, end=' ')
    for w in G[v] :
        if not visited[w] :
            dfsr(w)



G = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [3, 6]]
visited = [0] * 8

dfs(1)
result = 0
# dfsr(1)
