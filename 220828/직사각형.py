for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')

    if x1 == p2 or p1 == x2:
        if y1 == q2 or y2 == q1:
            print('c')

        else:
            print('b')

    if y2 == q1 or q2 == y1:
        print('b')

    else:
        print('a')