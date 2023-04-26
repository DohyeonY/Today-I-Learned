# from itertools import permutations

N, M = map(int, input().split())
lst = []
# for i in range(1, N+1) :
#     lst.append(str(i))
# # lst = map(str, range(1, N+1))
# # print(permutations(lst, M))
# # print(lst)
# print('\n'.join(list(map(' '.join, permutations(lst, M)))))


visited = [False] * (N + 1)

def dfs(a) :
    if a - 1 == M :
        print(' '.join(map(str, lst)))
        return
    
    for i in range(1, N+1) :
        if not visited[i] :
            visited[i] = True
            lst.append(i)
            dfs(a+1)
            visited[i] = False
            lst.pop()


dfs(1)