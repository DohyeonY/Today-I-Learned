W, H = map(int, input().split())            # 전체 가로 세로
N = int(input())                            # 상점의 갯수

def caldist(D, L) :
    if D == 1:
        return L
    elif D == 2:
        return H + W + (W - L)
    elif D == 3:
        return W + H + W + (H - L)
    else :
        return W + L
store = []
for _ in range(N) :
    lst = list(map(int, input().split()))        # D = 동서남북 L = 거리
    store.append(lst)

DD, DL = map(int, input().split())          # 동근이의 위치

total = 0
dong = caldist(DD, DL)

for i in range(N) :
    dist1 = caldist(store[i][0], store[i][1])
    path1 = abs(dong - dist1)
    path2 = 2 * W + 2 * H - path1
    if path1 < path2 :
        total += path1

    else :
        total += path2

print(total)

