def to_min(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def solution(book_time):
    arr = []
    
    for s, e in book_time :
        s = to_min(s)
        e = to_min(e) + 10
        arr.append((s, 's'))
        arr.append((e, 'e'))

    arr.sort()
    cnt = 0
    max_cnt = 0
    
    for val, flag in arr :
        if flag == 's' :
            cnt += 1
        else:
            cnt -= 1
        max_cnt = max(cnt, max_cnt)

    return max_cnt