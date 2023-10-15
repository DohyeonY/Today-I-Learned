def solution(s):
    lst = []

    for i in range(len(s)) :
        if s[i] == '(' :
            lst.append('(')
        else:
            if len(lst) == 0:
                return False
            else:
                lst.pop()

    return len(lst) == 0