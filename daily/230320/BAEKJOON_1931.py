'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
import sys

Num = int(sys.stdin.readline())
arr = [[0] * 2 for _ in range(Num)]
for i in range(Num) :
    start, end = map(int, sys.stdin.readline().split())
    arr[i][0] = start
    arr[i][1] = end
# print(arr)
# arr.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end_time = arr[0][1]
for i in range(1, Num) :
    if arr[i][0] >= end_time :
        cnt += 1
        end_time = arr[i][1]

# print(key)

print(cnt)