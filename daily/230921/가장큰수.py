def solution(numbers):
    answer = ''
    lst = []
    for i, num in enumerate(numbers):
        lst.append([str(num) * 4, i])

    lst.sort(reverse = True) 

    for i in lst:
        answer += str(numbers[i[1]])
    
    return "0" if answer < "1" else answer