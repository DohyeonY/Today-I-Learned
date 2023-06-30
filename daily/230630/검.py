def solution(number, limit, power):
    result = 1
    for i in range(2, number+1) :
        cnt = 0
        for j in range(1, int(i ** ( 1 / 2 )) + 1) :
            if i % j == 0 :
                if j == i // j:
                    cnt += 1
                else :
                    cnt += 2
            if cnt > limit :
                cnt = power
                break
        result += cnt
    return result