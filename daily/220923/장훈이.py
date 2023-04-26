import sys
sys.stdin=open("장훈이.txt", "r")

from itertools import permutations, combinations
T = int(input())

for tc in range(1, T+1) :
    N, B = input().split()
    lst = list(map(int, input().split()))
    checklst = []
    for j in range(1, int(N)+1) :                       # 모든 부분집합을 추려내기위해 1~N까지 j
        for i in combinations(lst, j) :                 # i에 lst에서 가질수있는 모든 부분집합들 담기
            i = list(i)                                 # i 리스트화 후 더해준다
            i = sum(i)
            if i >= int(B) :                            # i가 B보다 크거나 같으면 checklst에 추가해준다
                checklst.append(i)

    print(f'#{tc} {min(checklst) - int(B)}')
