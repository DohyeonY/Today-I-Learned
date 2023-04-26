import sys
sys.stdin=open("cardcnt.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    cards = input()
    # print(cards)
    resS = resD = resC = resH = 0
    Slst = [0] * 14
    Dlst = [0] * 14
    Hlst = [0] * 14
    Clst = [0] * 14

    for i in range(0, len(cards), 3) : # 0, 3, 6, 9....
        a, b = i+1, i+2
        if cards[i] == 'S' :              # 각 스페이스, 다이아, 하트, 클로버일때
            Slst[int(cards[a] + cards[b])] += 1
        elif cards[i] == 'D' :
            Dlst[int(cards[a] + cards[b])] += 1
        elif cards[i] == 'H' :
            Hlst[int(cards[a] + cards[b])] += 1
        elif cards[i] == 'C' :
            Clst[int(cards[a] + cards[b])] += 1

    result = ''
    for k in range(14) :
        if Slst[k] > 1 or Dlst[k] > 1 or Hlst[k] > 1 or Clst[k] > 1 :
            result = 'ERROR'
            break

        else :
            resS = 13 - sum(Slst)
            resD = 13 - sum(Dlst)
            resH = 13 - sum(Hlst)
            resC = 13 - sum(Clst)

    if result == 'ERROR':
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} {resS} {resD} {resH} {resC}')