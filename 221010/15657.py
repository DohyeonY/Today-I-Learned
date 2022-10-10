from itertools import combinations_with_replacement

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted(lst)

for i in list(combinations_with_replacement(lst, M)) :
    for j in i :
        print(j, end=' ')
    print()