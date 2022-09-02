import sys
sys.stdin=open("tournament.txt", "r")

def winner(i, j) :
    # if 영역의 데이터가 한개일때 :
    if i == j :
        # return 한개의위치
        return i
    lw = winner(i, (i+j)//2)
    rw = winner((i+j)//2+1, j)
    # if lw와 rw의 우승자를 결저하여 위치를 return
    if People[lw] == People[rw] :                     # 낸게 같을때 왼쪽이 이긴거
        return lw
    elif People[lw] == 1 and People[rw] == 2 :        # 가위바위보 경우의수
        return rw
    elif People[lw] == 1 and People[rw] == 3 :
        return lw
    elif People[lw] == 2 and People[rw] == 3 :
        return rw
    elif People[lw] == 2 and People[rw] == 1 :
        return lw
    elif People[lw] == 3 and People[rw] == 1 :
        return rw
    elif People[lw] == 3 and People[rw] == 2 :
        return lw

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    People = list(map(int, input().split()))

    # IDX값으로 계쏙 처리햇어서 +1 해줘서 몇번째 사람인지 확인
    print(f'#{tc} {winner(0, N-1) +1}')



