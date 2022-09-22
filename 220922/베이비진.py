import sys
sys.stdin=open("베이비진.txt", "r")

a = [1, 2, 3]
b = [2, 3, 4]
c = [3, 4, 5]
d = [4, 5, 6]
e = [5, 6, 7]
f = [6, 7, 8]
g = [7, 8, 9]
aa = [1, 1, 1]
bb = [2, 2, 2]
cc = [3, 3, 3]
dd = [4, 4, 4]
ee = [5, 5, 5]
ff = [6, 6, 6]
gg = [7, 7, 7]
hh = [8, 8, 8]
ii = [9, 9, 9]
jj = [0, 0, 0]
kk = [0, 1, 2]

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
            for j in range(0, len(playerOne)-3) :
                if playerOne[j : j+3] == a or playerOne[j : j+3] == b or playerOne[j : j+3] == c or playerOne[j : j+3] == d or playerOne[j : j+3] == e or playerOne[j : j+3] == f or playerOne[j : j+3] == g or playerOne[j : j+3] == aa or playerOne[j : j+3] == bb or playerOne[j : j+3] == cc or playerOne[j : j+3] == dd or playerOne[j : j+3] == ee or playerOne[j : j+3] == ff or playerOne[j : j+3] == gg or playerOne[j : j+3] == hh or playerOne[j : j+3] == ii or playerOne[j : j+3] == jj or playerOne[j : j+3] == kk :
                    result = 1
                    break
        playerTwo.append(lst[i+1])
        playerTwo.sort()
        # 같은 카드를 가졌을때 플레이어1이 이기지 못했을때 플레이어2의 패 전부 다 돌려서 하나라도 맞으면 플레이어2 승리
        if len(playerTwo) >= 3 :
            for j in range(0, len(playerTwo)-3) :
                if playerTwo[j : j+3] == a or playerTwo[j : j+3] == b or playerTwo[j : j+3] == c or playerTwo[j : j+3] == d or playerTwo[j : j+3] == e or playerTwo[j : j+3] == f or playerTwo[j : j+3] == g or playerTwo[j : j+3] == aa or playerTwo[j : j+3] == bb or playerTwo[j : j+3] == cc or playerTwo[j : j+3] == dd or playerTwo[j : j+3] == ee or playerTwo[j : j+3] == ff or playerTwo[j : j+3] == gg or playerTwo[j : j+3] == hh or playerTwo[j : j+3] == ii or playerTwo[j : j+3] == jj or playerTwo[j : j+3] == kk :
                    result = 2
                    break

    print(f'#{tc} {result}')