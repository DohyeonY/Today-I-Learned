from itertools import permutations,combinations

N, M = map(int, input().split())
lst = []
for i in range(1, N+1) :
    lst.append(str(i))
# set(lst)
# lst = map(str, range(1, N+1))
# print(permutations(lst, M))
# print(lst)

print('\n'.join(list(map(' '.join, combinations(lst, M)))))