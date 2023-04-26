# 데이터 구조의 복습 및 기본 사용
def fn_d(n) :
    
    a = list(str(n))
    result = 0

    for i in a :
        result += int(i)
    result = result + n

    return result

print(fn_d(2))

def is_selfnumber(n):

    for i in range(n):

        if fn_d(i) == n:
            return False

    return True

print(is_selfnumber(2))
