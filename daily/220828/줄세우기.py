N = int(input())

lst = list(map(int, input().split()))
line = []
# print(lst)

# line[-1] = 1



for i in range(N) :
    line.insert(i-lst[i], i+1)

print(*line)