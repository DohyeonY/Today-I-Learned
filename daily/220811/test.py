import sys
sys.stdin=open("ladder.txt", "r")

T = 10
for tc in range(1, T+1):
    input()
    Matrix = []  # 100X100
    for _ in range(100):
        N = list(map(int, ('0' + input() + '0').split()))
        Matrix.append(N)

    for i in range(102):
        if Matrix[99][i] == 2:  # 도착점
            pos_r = 99
            pos_c = i
            break

    while pos_r > 0:
        Matrix[pos_r][pos_c] = 0
        if Matrix[pos_r][pos_c - 1] == 1:
            pos_c = pos_c - 1

        elif Matrix[pos_r][pos_c + 1] == 1:
            pos_c = pos_c + 1

        else:
            pos_r = pos_r - 1

    sol = pos_c

    print(f'#{tc} {sol}')