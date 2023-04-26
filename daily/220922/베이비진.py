# import sys
# sys.stdin=open("베이비진.txt", "r")

checklst = [[1, 2, 3],[2, 3, 4],[3, 4, 5],[4, 5, 6],[5, 6, 7],[6, 7, 8],[7, 8, 9],[1, 1, 1],[2, 2, 2],[3, 3, 3],[4, 4, 4],[5, 5, 5],[6, 6, 6],[7, 7, 7],[8, 8, 8],[9, 9, 9],[0, 0, 0],[0, 1, 2]]

T = int(input())

for tc in range(1, T+1) :
    lst = list(map(int, input().split()))
    playerOne = []
    playerTwo = []
    # 아무도 못이기면 result는 변하지 않음
    result = 0
    # 받아온 정보를 플레이어1과 2의 패로 나누고 정렬함
    for i in range(0, len(lst), 2) :
        playerOne.append(lst[i])
        playerOne.sort()
        # 정렬 될때마다 + 패가 3장이상일때 있는 패 전부 다 돌려서 하나라도 맞으면 플레이어1 승리
        if len(playerOne) >= 3 :
            for j in range(0, len(playerOne)-2) :
                if playerOne[j : j+3] in checklst :
                    result = 1
                    break
            setlst = set(playerOne)
            setlst = list(setlst)
            setlst.sort()
            if len(setlst) >= 3:
                for k in range(0, len(setlst)-2) :
                    if setlst[k : k+3] in checklst :
                        result = 1
                        setlst = []
                        break
        if result != 0 :
            break
        playerTwo.append(lst[i+1])
        playerTwo.sort()
        # 같은 카드를 가졌을때 플레이어1이 이기지 못했을때 플레이어2의 패 전부 다 돌려서 하나라도 맞으면 플레이어2 승리
        if len(playerTwo) >= 3 :
            for j in range(0, len(playerTwo)-2) :
                if playerTwo[j : j+3] in checklst :
                    result = 2
                    break
            setlst = set(playerTwo)
            setlst = list(setlst)
            setlst.sort()
            if len(setlst) >= 3:
                for k in range(0, len(setlst)-2) :
                    if setlst[k : k+3] in checklst :
                        result = 2
                        setlst = []
                        break
        if result != 0 :
            break
    print(f'#{tc} {result}')