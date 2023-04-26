def myreverse(s):
    s = list(s)
    N = len(s)
    for i in range(N//2):
        s[i], s[N-1-i] = s[N-1-i], s[i]

    s = ''.join(s)

    return s



print(myreverse('abcde'))