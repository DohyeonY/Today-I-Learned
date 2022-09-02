'''
row = [0, r]
column = [0, c]
로 받는 것
(x,y축처럼 생각해주기)

'''


W, H = map(int, input().split())

N = int(input())
arr = []
for _ in range(N) :
    lst = list(map(int, input().split()))
    arr.append(lst)

Row = [0, W]
Col = [0, H]
for i in range(N) :
    if arr[i][0] == 0 :
        Col.append(arr[i][1])
    else :
        Row.append(arr[i][1])

Row.sort()
Col.sort()
# print(Row, Col)
cutrow = []
cutcol = []
for i in range(len(Row)-1) :
    cutrow.append(Row[i+1] - Row[i])
for i in range(len(Col)-1) :
    cutcol.append(Col[i+1] - Col[i])
#
# print(cutrow, cutcol)

print(max(cutrow) * max(cutcol))