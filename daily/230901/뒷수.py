def solution(numbers):
    answer = []
    stack = []
    numbers.reverse()
    
    for num in numbers :
        if not stack :
            stack.append(num)
            answer.append(-1)
        else:
            while True :
                if not stack:
                    stack.append(num)
                    answer.append(-1)
                    break

                last_idx = len(stack) -1
                
                if stack[last_idx] <= num:
                    stack.pop()
                else: 
                    answer.append(stack[last_idx])
                    stack.append(num)
                    break
    answer.reverse()
    return answer