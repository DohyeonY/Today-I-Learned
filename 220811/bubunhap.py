import sys
sys.stdin=open("bubunhap.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, K = map(int,input().split())

#     # print(K)
#     arr = []
# N = 12
    arr = [1,2,3,4,5,6,7,8,9,10,11,12]
    n = len(arr)
    cnt = 0
    # sumv = 0
    # cntv = 0
    for i in range(1<<n):
        sumv = 0
        cntv = 0

        for j in range(n) :

            if i & (1<<j) :
                sumv += arr[j]
                cntv += 1

        if sumv == K and cntv == N :
            cnt += 1

    print(f'#{tc} {cnt}')

        # arr[0] = i
        # for j in range(N) :
        #     arr[1] = j
        #     for k in range(N) :
        #         arr[2] = k
        #         for l in range(N) :
        #             arr[3] = l
        #             print(arr)
# n = len(arr)  # n : 원소의 개수

    # for i in range(1<<N) :    # 1 << N : 원소가 N개일 경우의 모든 부분 집합의 개수
    #     # print(i)
    #      for j in range(N) :  # 원소의 수만큼 비트를 비교
    #          # print(j)
    #          if i & (1<<j) :  # i의 j번 비트가 1인 경우
    #              print(arr[j])
    #      print()
    # print()


# bit = [0,0,0,0]
# for i in range(2) :
#     bit[0] = i
#     for j in range(2) :
#         bit[1] = j
#         for k in range(2) :
#             bit[2] = k
#             for l in range(2) :
#                 bit[3] = l
                # print(bit)


