# def perm(k, midSum, s) :
#     global minV
#     if k == N :


#         minV = min(minV, minSum)
#         return
#     for i in range(N) :
#         if visited[i] :
#             continue
#         # result[k] = i
#         # s = result[k - 1]
#         visited[i] = True
#         perm(k+1, midSum+ARR[s][i], i)
#         visited[i] = False
# N = 5
# visited = [False] * N
# result = [-1] * N
# visited[0] = True
# result[0] = 0
# perm(1, 0, 0)

a = [1, 1, 1, 3]
setlst = set(a)
print(a)
print(setlst)