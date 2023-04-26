import sys
sys.stdin=open("mirror.txt", 'r')

T = int(input())

for tc in range(1, T+1) :
    mi = input()
    mi = list(mi)
    N = len(mi)
    for i in range(N//2):
        mi[i], mi[N-1-i] = mi[N-1-i], mi[i]

    for j in range(N) :
        if mi[j] == 'b' :
            mi[j] = 'd'
        elif mi[j] == 'd' :
            mi[j] = 'b'
        elif mi[j] == 'q':
            mi[j] = 'p'
        elif mi[j] == 'p' :
            mi[j] = 'q'
    mi = ''.join(mi)






    print(f'#{tc} {mi}')