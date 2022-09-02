for _ in range(4) :
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    result = 'a'
    if q1 < y2 or q2 < y1 or x1 > p2 or p1 < x2 :
        result = 'd'
    if p1 == x2 :
        result = 'c' if (q1 == y2 or q2 == y1) else 'b'
    if x1 == p2 :
        result = 'c' if (q1 == y2 or q2 == y1) else 'b'
    if y1 == q2 :
        result = 'c' if (p1 == x2 or p2 == x1) else 'b'
    if y2 == q1 :
        result = 'c' if (p1 == x2 or p2 == x1) else 'b'

    print(result)