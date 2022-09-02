# 데이터 구조의 복습 및 기본 사용

def leap_year(a):
    stt = (f'{a}년은 윤년입니다.')
    sttt = (f'{a}년은 윤년이 아닙니다.')
    if a % 4 == 0 and a % 100 != 0 :
        return stt
    elif a % 400 == 0 :
        return stt
        
    else :
        return sttt

print(leap_year(2021))
print(leap_year(2020))
