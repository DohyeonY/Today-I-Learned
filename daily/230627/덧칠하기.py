def solution(n, m, section):
    result = 1
    firstSection = section[0]
    for i in section:
        if firstSection + m <= i:
            result += 1
            firstSection = i
    return result