def ne(month, cost) :
    global mincost

    if month >= 12 :
        if mincost > cost :
            mincost = cost
        return
    ne(month + 1, cost + day * table[month])
    ne(month + 1, cost + onem)
    ne(month + 3, cost + threem)

T = int(input())

for tc in range(1, T+1) :
    day, onem, threem, year = map(int, input().split())
    table = list(map(int, input().split()))

    mincost = year

    ne(0, 0)

    print(f'#{tc} {mincost}')