# 데일리 실습 과제 5-1 요청과 응답에 따른 데이터 수집

fruits = list(input().lower().split(",")) # 소문자로 입력 ,로 구분
for i in range(len(fruits)):     
    if "rotten" in fruits[i]:        # rotten이 리스트 요소 중 있으면 7번째 단어부터 출력 아니면 그냥 출력
        fruits[i] = fruits[i][6:]
print(fruits)

# stv
