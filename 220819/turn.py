def turnd(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = a[i][j]
    return new