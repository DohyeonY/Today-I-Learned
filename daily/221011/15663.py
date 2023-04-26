from itertools import permutations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

result = []
for i in list(permutations(lst, M)):
    result.append(i)

result = sorted(list(set(result)))

for i in result :
    for j in i :
        print(j, end = " ")
    print()