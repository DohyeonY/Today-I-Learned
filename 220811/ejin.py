import sys
sys.stdin=open("ejin.txt", "r")

def ejin(P, K) :
    start = 1
    end = P
    cnt = 0

    while start <= end :
        mid = int((start + end) / 2)
        cnt += 1
        if mid == K :
            return cnt

        elif mid > K :
            end = mid

        else :
            start = mid


T = int(input())

for tc in range(1, T+1) :
    page, aa, bb= map(int, input(). split())

    if ejin(page, aa) < ejin(page, bb):
        print(f'#{tc} A')
    elif ejin(page, aa) == ejin(page, bb):
        print(f'#{tc} 0')
    else :
        print(f'#{tc} B')








# T = int(input())
#
# for i in range(1, T+1) :
#     P, Pa, Pb = list(map(int,input().split()))
#
#     start = 0
#     end = P
#     while start <= end :
#         pm = (start + end) // 2
#         if pm == Pa and pm == Pb:
#             print('0')
#             break
#
#         elif pm == Pa :
#             print("B")
#             break
#         elif pm == Pb :
#             print("A")
#             break
#         elif pm < Pa :
#             start = pm
#
#         elif pm > Pa :
#             end = pm
#
#         elif pm > Pb:
#             end = pm
#
#         elif pm < Pb :
#             start = pm


