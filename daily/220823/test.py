T= int(input())

for tc in range(1,1+T):

    N,M = map(int,input().split())

    lst = [list(map(int,input().split())) for _ in range(N)]

    maxn=0
    for i in range(N):
        cnt=0
        for j in range(M):
            if lst[i][j] ==1:
                cnt+=1
            else:
                cnt=0
            if maxn<cnt:
                maxn=cnt
    for i in range(M) :
        cnt1=0
        for j in range(N):
            if lst[j][i]==1:
                cnt1+=1
            else:
                cnt1=0
            if maxn<cnt1:
                maxn=cnt1

    print(f'#{tc} {maxn}')