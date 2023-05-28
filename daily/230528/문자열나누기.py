def solution(s):
    result = 0
    cnt = 0
    secondCnt = 0
    first_chr = ''
    
    for i in s:
        if first_chr == '' :
            first_chr = i
            cnt += 1
            continue
        
        if i == first_chr :
            cnt += 1
        else:
            secondCnt += 1
        
        if cnt == secondCnt :
            result += 1
            cnt, secondCnt = 0, 0
            first_chr = ''
            
    if first_chr:
        result += 1
        
    return result