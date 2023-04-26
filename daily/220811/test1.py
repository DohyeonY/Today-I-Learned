import sys
sys.stdin=open("ladder.txt", "r")

for tc in range(1, 11):
    aa = input()
    sadari = []  # 100X100
    for _ in range(100):
        lst = list(map(int, ('0' + input() + '0').split()))
        sadari.append(lst)

    for i in range(102):
        if sadari[99][i] == 2:  # 도착점
            starty = 99
            startx = i
            break

    while starty > 0:
        sadari[starty][startx] = 0
        if sadari[starty][startx - 1] == 1:
            startx = startx - 1

        elif sadari[starty][startx + 1] == 1:
            startx = startx + 1

        else:
            starty = starty - 1

    endx = startx

    print(f'#{tc} {endx}')