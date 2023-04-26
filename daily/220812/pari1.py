import sys
sys.stdin=open("pari.txt", "r")

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))


    maxV = 0
    for y in range(N-M+1):
        for x in range(N-M+1):
            temp = 0
            for my in range(M):
                for mx in range(M):
                    temp += arr[y+my][x+mx]
            if maxV < temp:
                maxV = temp
    print(f'#{t+1} {maxV}')