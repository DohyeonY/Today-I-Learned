def solution(k, tangerine):
    answer = 0
    arr = {}
    
    for i in tangerine :
        if i in arr :
            arr[i] += 1
        else:
            arr[i] = 1
    arr = dict(sorted(arr.items(), key = lambda x : x[1], reverse = True))
    for i in arr :
        if k <= 0 :
            return answer
        k -= arr[i]
        answer += 1
    return answer