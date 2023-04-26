import sys
sys.stdin=open("maxmin.txt", 'r')


TC = int(input())

# print(ai)

for tc in range(1, TC+1) :
    n = int(input())
    ai = list(map(int, input().split()))
    maxv = 0
    minv = 1000001
    for i in range(0, n) :
        # print(i)

        if ai[i] > maxv :
            maxv = ai[i]
            # print(maxv)
        
        if ai[i] < minv :
            minv = ai[i]

    print(f'#{tc} {maxv-minv}')