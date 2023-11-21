def check(s):
    stack = []
    
    for i in s :
        if len(stack) == 0 : 
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(": stack.pop()
            elif i == "]" and stack[-1] == "[": stack.pop()
            elif i == "}" and stack[-1] == "{": stack.pop()
            else: stack.append(i)
    if len(stack) == 0:
        return 1
    else :
        return 0
        
        
def solution(s):
    result = 0
    
    for i in range(len(s)) :
        if check(s): result += 1
        s = s[1:] + s[:1]
        
    return result