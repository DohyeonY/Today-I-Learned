G = {'A': ['B', 'C'], 'B':['A', 'D', 'E'], 'C':['A', 'E'],
    'D':['B', 'F'], 'E':['B', 'C', 'F'], 'F':['D', 'E', 'G'], 'G':['F']}

# 'A' => 0
# 'B' => 1
#ord(w) - ord('A')

def dfs(v) :
    visited = [False] * 7
    ST = []

    print(v)
    visited[ord(v)-ord('A')] = True
    ST.append(v)

    while len(ST) :
        v = ST.pop()
        for w in G[v] :
            if visited[ord(w) - ord('A')] == False :
                ST.append(w)
                print(w)
                visited[ord(w) - ord('A')] = True


dfs('A')