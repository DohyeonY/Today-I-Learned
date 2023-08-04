def solution(survey, choices):
    answer = ''
    n = len(survey)
    personality = {'R' : 0, 'T' : 0, 'C' : 0, 'F' : 0, 'J' : 0, 'M' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(n) :
        first, second = survey[i][0], survey[i][1]
        if choices[i] <= 3 :
            personality[first] += 4 - choices[i]
        elif choices[i] > 4 :
            personality[second] += choices[i] - 4
    
    if personality['R'] >= personality['T'] :
        answer += 'R'
    else:
        answer += 'T'
    
    
    if personality['C'] >= personality['F'] :
        answer += 'C'
    else:
        answer += 'F'
        
    
    if personality['J'] >= personality['M'] :
        answer += 'J'
    else:
        answer += 'M'
        
    
    if personality['A'] >= personality['N'] :
        answer += 'A'
    else:
        answer += 'N'
        
    # print(personality)
    return answer