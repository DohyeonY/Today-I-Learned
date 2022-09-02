Round = int(input())

for _ in range(Round) :
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    lsta = [a.count(4), a.count(3), a.count(2), a.count(1)]
    lstb = [b.count(4), b.count(3), b.count(2), b.count(1)]
    if lsta[0] > lstb[0] :
        print('A')
    elif lsta[0] < lstb[0] :
        print('B')
    elif lsta[1] > lstb[1] :
        print('A')
    elif lsta[1] < lstb[1] :
        print('B')
    elif lsta[2] > lstb[2] :
        print('A')
    elif lsta[2] < lstb[2] :
        print('B')
    elif lsta[3] > lstb[3] :
        print('A')
    elif lsta[3] < lstb[3] :
        print('B')
    else :
        print('D')
