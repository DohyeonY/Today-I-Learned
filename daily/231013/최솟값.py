def solution(a, b):
    answer = 0

    a.sort()
    b.sort(reverse = True)

    for i in range(len(a)) :
        answer += (a[i] * b[i])

    return answer