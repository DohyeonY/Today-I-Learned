import sys
sys.stdin=open("numcard.txt","r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ai = input()
    cnt = [0] * 101


    for i in ai:
        # print(i)
        cnt[int(i)] += 1
    print(cnt)

    num = 0
    ct = 0

    for i in range(101):

        if ct <= cnt[i] :  # cnt에 들어있는 갯수의 최대값이면

            num = i
            ct = cnt[i]

    print(f'#{tc} {num} {ct}')






