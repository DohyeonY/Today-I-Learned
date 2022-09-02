# 객체지향 프로그래밍의 이해와 기...

def collatz(num) :
    count = 0

    while count <= 500 :

        if num % 2 == 0 :
            num = num // 2
            count += 1

        elif num % 2 == 1 :
            num = num * 3 + 1
            count += 1

        if num == 1 :
            return f'{count}번 만에 1이 되었습니다.'
        # print(num)
    # return 1
    
    return -1

print(collatz(6))
print(collatz(512))
print(collatz(500))
print(collatz(654168451613131515641684616546516516511035))