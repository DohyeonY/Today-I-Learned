'''
풀이 방법
7명의 난쟁이의 키의 합은 항상 100이다.
그럼 9명이라는 적은 숫자에서 2명을 빼는
모든 경우의 수 중 100인 경우일 때
2명을 검거하면 되는 간단한 문제
'''


tall = []
for _ in range(9) :                               # 총 9명의 난쟁이의 키를 받기위한 for문
    M = int(input())                              # 키 입력
    tall.append(M)                                # 입력 받은걸 리스트화 시켜줌
    tall.sort()                                   # 오름차순으로 출력해야하니까 미리 sort시켜줌
# print(tall)
murder1 = 0
murder2 = 0
for i in range(0, 9) :                            # 2명의 난쟁이를 찾고 난쟁이들을 전부 확인하기 위해 for문 2개를 씀
    for j in range(1, 9) :                        # 지금까지의 2차원 배열과는 다르게 같은 애들을 빼는건 의미가 없어서 i의 다음값부터 시작

        if sum(tall) - (tall[i] + tall[j]) == 100 : # 누군지 몰라도 난쟁이 2명을 뺀 값이 100이면 된다
            murder1 = tall[i]                       # 검거해서 추가해줌
            murder2 = tall[j]

tall.remove(murder1)                                # 함수 마구써서 제거해버림
tall.remove(murder2)

for result in tall :                                # 일자로 출력하라해서 이렇게함
    print(result)

