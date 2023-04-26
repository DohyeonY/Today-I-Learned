# 크롤링을 통한 서비스 개발 예제 5
# 반복문 사용
def sum_of_digit(num) :
    result = 0
    while num > 0 :
        result += num % 10
        num = num // 10
    return result

x = int(input())
print(sum_of_digit(x)) 

# 다른풀이
sum(map(int,'12345'))