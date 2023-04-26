import sys
sys.stdin=open("ladder.txt", "r")


T = 10
# sadari = []
for tc in range(1, T+1) :
    aa = input()
    n = 100
    sadari = []
    for _ in range(n) :
        lst = list(map(int, ('0' + input() + '0').split()))
        # 좌우로 넘어가는거 생각해서 더미값을 하나씩 넣어준것 그러나 파이썬만 되고 다른언어는 안된다
        sadari.append(lst)
        # print(sadari)

    startx = 0
    starty = 0
    for i in range(n+2):
        if sadari[n-1][i] == 2 :   # starting point
            startx = i
            starty = n-1
            break

    # for starty in range(99, 0, -1) :
    while starty > 0 :
        sadari[starty][startx] = 0   # 지나간 자리 0으로 변환
        if sadari[starty][startx-1] == 1 :           # 왼쪽에 1이 있으면 거기로 옮기기
            # while
            startx = startx-1

        elif sadari[starty][startx+1] == 1 :   # 오른쪽에 1이 있으면 거기로 옮기기

            startx = startx + 1

        else :   # 암것도 없으면 위로 직진

            starty = starty -1

    print(f'#{tc} {startx}')