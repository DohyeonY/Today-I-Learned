# 찾으면 패턴의 시작위치를 리턴하고
# 못찾으면 -1을 턴하는 함수를 만들어라

def find(t, p) :
    # t = list(t)
    # p = list(p)
    j = 0
    i = 0
    while j < M and i < N:
        if t[i] == p[j] :
            i += 1
            j += 1

        else :
            i -= j
            j = 0
            i += 1

    if j == M :
        return i - M
    else :  # i == N
        return -1




t = 'a pattern matching algorithm test'
p = 'rithm'
N = len(t)
M = len(p)
print(find(t, p))