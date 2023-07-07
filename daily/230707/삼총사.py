def solution(number):
    answer = 0
    students = len(number) 
    
    for i in range(students - 2) :
        for j in range(i + 1, students - 1) :
            for k in range(j + 1, students) :
                if number[i] + number[j] + number[k] == 0 :
                    answer += 1
    return answer