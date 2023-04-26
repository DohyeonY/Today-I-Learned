from hashlib import new
import sys
from tkinter import N
sys.stdin=open("최대상금.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    Num, Cnt = input().split()                      # 숫자판의 정보, 교환횟수
    changeNum = set([Num])                          # 입력받은 숫자들의 위치를 변경한 값 중 중복된걸 빼주기 위해 set 사용
    newNum = set()                                  # 위와 마찬가지
    for _ in range(int(Cnt)) :                      # 진행해 나가는 과정이 changNum의 값을 하나씩 이동하여 모든 경우의 수를 newNum으로 옮기는게 목표라서
                                                    # changeNum의 값이 존재하지 않으면 모든 경우의 수가 newNum에 있다는 말
        while changeNum :                           # changNum에서 값 하나를 가져와서 리스트화 시킴
            s = changeNum.pop()
            s = list(s)
            for i in range(len(Num)) :              # 숫자의 길이 만큼 바꿀수 있는 모든 숫자를 다 바꿔봄
                for j in range(i+1, len(Num)) :
                    s[i], s[j] = s[j], s[i]         # 바꾸고
                    newNum.add(''.join(s))          # 그 값을 newNum에 집어넣음
                    s[i], s[j] = s[j], s[i]         # 다음 경우의 수도 계산해야하기 때문에 s의 값을 초기화

        changeNum,newNum = newNum,changeNum         # for문을 끝내기 전에 newNum에 있는 모든 경우의 수를 다시 changeNum으로 옮기고 다음 카운트를 진행함

    changeNum = map(int, changeNum)
    result = max(changeNum)

    print(f'#{tc} {result}')