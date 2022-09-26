def merge(lLst, rLst) :
    global cnt
    lp = rp = 0
    result = []
    while lp < len(lLst) and rp < len(rLst) :
        if lLst[lp] < rLst[rp] :
            result.append(lLst[lp])
            lp += 1
        else :
            result.append(rLst[rp])
            rp += 1
    if lLst[-1] > rLst[-1] :
        cnt += 1
    result.extend(lLst[lp:])
    result.extend(rLst[rp:])
    return result

def merge_s(lst) :
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_s(lst[:mid])
    right = merge_s(lst[mid:])
    return merge(left, right)

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    lst = list(map(int, input().split()))
    mid = N // 2
    cnt = 0
    result = merge_s(lst)
    print(f'#{tc} {result[mid]} {cnt}')