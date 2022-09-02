numOfmychu = 20
Q = []
n = 1
Q.append(n)
cnt = [0] * 1000
remain = 20
while remain > 0 :
    t = Q.pop(0)
    cnt[t] += 1
    remain -= cnt[t]
    Q.append(t)
    n += 1
    Q.append(n)
    print(t, '학생 => ', cnt[t], Q)    
