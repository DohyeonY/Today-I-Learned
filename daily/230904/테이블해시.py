def solution(data, col, row_begin, row_end):
    answer = 0
    data = sorted(data, key = lambda x: [x[col - 1], -x[0]])
    
    for i in range(row_begin, row_end + 1) :
        total = 0
        for j in data[i - 1] :
            total += (j % i)
        answer ^= total
            
    return answer