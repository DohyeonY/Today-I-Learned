# from itertools import permutations

# N, M = map(int, input().split())
# lst = sorted(list(map(str, input().split())))

# # for i in permutations(lst, M) :
# #     print(''.join(i))

# print('\n'.join(list(map(' '.join, permutations(lst, M)))))


from pydoc import visiblename


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [False] * N
stack = []

def dfs() :
    if len(stack) == M :
        print(' '.join(map(str, stack)))
        return

    for i in range(N) :
        if not visited[i] :
            stack.append(lst[i])
            visited[i] = True
            dfs()
            visited[i] = False
            stack.pop()

dfs()
