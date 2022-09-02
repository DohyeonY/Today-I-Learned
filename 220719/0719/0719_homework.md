### 1. Python 예약어
  and, exec, not, assert, finally, or, break, for, pass, class, from, print, continue, global, raise, def, if, return, del, import, try, elif, in, with, except, lambda, yield

### 2. 실수 비교
import math

num1 = 0.1 * 3
num2 = 0.3

math.isclose(num1, num2)

### 3. 이스케이프 스퀸스
\n # 줄바꿈
\t # 탭
\\ # 백슬래시

### 4. String Interpolation
name = '철수'

f'안녕, {name}야'

### 5. 형 변환
int('3.5')

### 6. 네모 출력
print('*'*5 + '\n' + '*'*5 + '\n'+ '*'*5 + '\n'+ '*'*5 + '\n'+ '*'*5 + '\n' +'*'*5 + '\n'+ '*'*5 + '\n'+ '*'*5 + '\n' +'*'*5)


### 7. 이스케이프 시퀸스 응용
print('"파일은 c:\Windows\\Users\내문서\Python에 저장이 되었습니다." \n나는 생각했다. \'cd를 써서 git bash로 들아가 봐야지.\'')

### 8. 근의 공식
D = ((b * b - 4 * a * c) ** 0.5)

x_1 = (-b + D) / (2 * a)

x_2 = (-b - D) / (2 * a)

print(x_1, x_2)