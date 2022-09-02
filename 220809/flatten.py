import sys
sys.stdin=open("flatten.txt", "r")

T = 10

for tc in range(1, T+1) :
    dump = int(input())
    he = list(map(int, input().split()))

    lst = [0] * 101
    maxv = 0
    minv = 101
    #
    for i in he :
        lst[i] += 1    # [ 몇층짜리 몇개씩 있는지 리스트화]
    # print(lst)
    # maxv = 0
    # minv = 101

        if i < minv :    # he의 요소 중 가장 높은 값을 maxv에 낮은값을 minv에 넣음
            minv = i
        if i > maxv :
            maxv = i

    # print(minv, maxv)
    n = 0               # 0부터 dump횟수까지 계속 뺑이돌리면서 max쪽은 하나 빼고 바로 한칸 낮아진거니까 한칸밑은 플러스
    while n < dump:    # min쪽은 반대로
        lst[maxv] -= 1
        lst[maxv-1] += 1
        lst[minv] -= 1
        lst[minv+1] += 1

        if lst[maxv] == 0:   # 근데 lst[max]값이 결국 0이 되어버리면 max값을 한칸 낮춰줌
            maxv -= 1

        if lst[minv] == 0:   # 건물이 0층이 있으면 while을 써야한다 하지만 0층이 없기때문에 if도 가능~
            minv += 1


        n += 1   # while을 끝내야하니 한바퀴당 n에 1씩 추가 = dump를 한번씩 진행한다는 의미

    print(f'#{tc} {maxv-minv}')

