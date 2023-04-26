def swim(idx, money):
    global min_price
    if idx >= 12:
        if money < min_price:  # 최소 비용 비교
            min_price = money
        return
    if plan[idx]:  # 운영 계획이 존재 할 때
        for i in range(4):  # 비용을 기준으로 탐색하므로 비용의 개수인 4번만큼 반복
            if i == 0:  # 1일권
                swim(idx + 1, money + price[i] * plan[idx])
            elif i == 1:  # 1달권
                swim(idx + 1, money + price[i])
            elif i == 2:  # 3개월권
                swim(idx + 3, money + price[i])
            else:  # 1년권
                swim(idx + 12, money + price[i])
    else:  # 운영계획이 존재 안한다면 idx를 1만큼 늘려서 다시 탐색
        swim(idx + 1, money)


T = int(input())
for t in range(T):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    min_price = 99999999

    swim(0, 0)
    print('#{} {}'.format(t + 1, min_price))