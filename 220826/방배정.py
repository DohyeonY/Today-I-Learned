# N = 학생수 room = 방 정원
N, room= map(int,input().split())
boy = [0] * 7
girl = [0] * 7
cnt = 0
for _ in range(N) :
    sex, grade = map(int, input().split())

    if sex == 0 :
        girl[grade] += 1
    else :
        boy[grade] += 1

# print(boy)
# print(girl)
for i in range(1, 7) :
    if boy[i] % room == 0 :                 # 짝수일때
        cnt += boy[i] // room
    else :                                  # 홀수일때
        cnt += boy[i] // room + 1

    if girl[i] % room == 0 :                 # 짝수일때
        cnt += girl[i] // room
    else :                                  # 홀수일때
        cnt += girl[i] // room + 1

print(cnt)
# print(N, room)
# print(lst)
# cnt = 0
# onemcnt = 0
# onewcnt = 0
# twomcnt = 0
# twowcnt = 0
# threemcnt = 0
# threewcnt = 0
# fourwcnt = 0
# fourmcnt = 0
# fivewcnt = 0
# fivemcnt = 0
# sixmcnt = 0
# sixwcnt = 0
# for i in range(N) :
#     #1학년
#
#     if lst[i][1] == 1 and lst[i][0] == 1:
#         onemcnt += 1
#     elif lst[i][1] == 1 and lst[i][0] == 0:
#         onewcnt += 1
#     #2학년
#
#     if lst[i][1] == 2 and lst[i][0] == 1:
#         twomcnt += 1
#     elif lst[i][1] == 2 and lst[i][0] == 0 :
#         twowcnt += 1
#     #3학년
#
#     if lst[i][1] == 3 and lst[i][0] == 1:
#         threemcnt += 1
#     elif lst[i][1] == 3 and lst[i][0] == 0 :
#         threewcnt += 1
#     #4학년
#
#     if lst[i][1] == 4 and lst[i][0] == 1:
#         fourmcnt += 1
#     elif lst[i][1] == 4 and lst[i][0] == 0 :
#         fourwcnt += 1
#     #5학년
#
#     if lst[i][1] == 5 and lst[i][0] == 1:
#         fivemcnt += 1
#     elif lst[i][1] == 5 and lst[i][0] == 0 :
#         fivewcnt += 1
#     #6학년
#
#     if lst[i][1] == 6 and lst[i][0] == 1:
#         sixmcnt += 1
#     elif lst[i][1] == 6 and lst[i][0] == 0 :
#         sixwcnt += 1
#
#
# if onemcnt % room == 0 :
#     cnt += onemcnt // 2
# else :
#     cnt += onemcnt // 2 + 1
# if onewcnt % room == 0 :
#     cnt += onewcnt // 2
# else :
#     cnt += onewcnt // 2 + 1
#
# if twomcnt % room == 0 :
#     cnt += twomcnt // 2
# else :
#     cnt += twomcnt // 2 + 1
# if twowcnt % room == 0 :
#     cnt += twowcnt // 2
# else :
#     cnt += twowcnt // 2 + 1
#
# if threemcnt % room == 0:
#     cnt += threemcnt // 2
# else:
#     cnt += threemcnt // 2 + 1
# if threewcnt % room == 0:
#     cnt += threewcnt // 2
# else:
#     cnt += threewcnt // 2 + 1
#
# if fourmcnt % room == 0 :
#     cnt += fourmcnt // 2
# else :
#     cnt += fourmcnt // 2 + 1
# if fourwcnt % room == 0 :
#     cnt += fourwcnt // 2
# else :
#     cnt += fourwcnt // 2 + 1
#
# if fivemcnt % room == 0 :
#     cnt += fivemcnt // 2
# else :
#     cnt += fivemcnt // 2 + 1
# if fivewcnt % room == 0 :
#     cnt += fivewcnt // 2
# else :
#     cnt += fivewcnt // 2 + 1
#
# if sixmcnt % room == 0 :
#     cnt += sixmcnt // 2
# else :
#     cnt += sixmcnt // 2 + 1
# if sixwcnt % room == 0 :
#     cnt += sixwcnt // 2
# else :
#     cnt += sixwcnt // 2 + 1
#
# print(cnt)