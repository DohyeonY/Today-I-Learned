# n = list(map(int, input().split()))

# for i in range(n, -1, -1) :
#     if i % 2 == 1 :
#
#         # print(i)

# print(n)

# for tc in range(10):
#     T, N = map(int, input().split())
#     arr = list(map(int, input().split()))

lst = [0, 0, 5, 1, 0, 2]
idxlst = []
vallst = []
for i in range(len(lst)):
    if i % 2 == 0:
        idxlst.append(lst[i])
    else:
        vallst.append(lst[i])

print(idxlst)
print(vallst)