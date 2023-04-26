import sys
sys.stdin=open("컨테이너운반.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    # N = 컨테이너 수, M = 트럭에 넣을 수 있는 무게
    N, M = map(int,input().split())
    #
    box = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    box.sort()
    truck.sort()
    # print(N,M)
    # print(box)
    # print(truck)
    sumbox = 0
    # 박스 트럭 둘 다 리스트에 값이 있을 때
    while box and truck :
        # 트럭 젤루 큰값 가져오고
        a = truck.pop()
        # 감당못하는 무게의 박스는 다 날려버리기 위해 다시한번 while문을 넣고 무한 반복 되는걸 막기 위해 제대로 적재되면 break로 빠져나감
        while box :
            s = box.pop()
            if a >= s :
                sumbox += s
                break

    print(f'#{tc} {sumbox}')





