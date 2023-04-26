### 1. 숫자의 입력과 출력
a, b = input().split()

a = int(a)
b = int(b)

print(a + b)

### 2. Dictionary를 활용하여 평균 구하기
lun = {'자장면' : '5000', '잠봉' : '6000', '당수육' : '12000'}

print((int(lun['자장면']) + int(lun['잠봉']) + int(lun['당수육'])) / 3)