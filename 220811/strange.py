import sys
sys.stdin=open("strange.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
#
    for i in range(N):  # 구간의 맨 끝 인덱스

        for j in range(i, N):  # 인접원소 중 왼쪽원소 인덱스

            if i % 2 == 0 and lst[i] < lst[j] :
                lst[i], lst[j] = lst[j], lst[i]

            elif i % 2 == 1 and lst[i] > lst[j] :
                lst[i], lst[j] = lst[j], lst[i]



    print(f'#{tc}', end=' ')

    for k in range(10) :
        print(f'{lst[k]}', end=' ')
    print()


    #
    # for i in range(N - 1, 0, -1):
    #     for j in range(i):
    #         if lst[j] > lst[j + 1]:
    #             lst[j], lst[j + 1] = lst[j + 1], lst[j]


    # print(lst)