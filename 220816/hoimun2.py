import sys
sys.stdin=open("hoimun2.txt", "r")

def turnd(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = a[i][j]
    return new

T = 10

for tc in range(1, T+1) :
    pan = []
    num = int(input())
    N = 100

    for _ in range(N) :
        lst = input()
        pan.append(lst)

    cnt = 1

    for row in pan :   # 가로비교
        for start in range(N) :   # 0~99
            for end in range(N+1) :
                if row[start : end] == row[start : end][::-1] :
                    if cnt < len(row[start : end]):
                        cnt = len(row[start : end])

    turnpan = turnd(pan)
    for col in turnpan :
        for start2 in range(N):
            for end2 in range(N+1) :        # end 에는 idx 98까지밖에 안들어가서 101 로 해줘야 아래 end2에 99까지 들어간다~
                if col[start2: end2] == col[start2: end2][::-1]:
                    if cnt < len(col[start2: end2]):
                        cnt = len(col[start2: end2])

    print(f'#{tc} {cnt}')