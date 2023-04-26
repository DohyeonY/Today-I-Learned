import sys
sys.stdin=open("findway.txt", "r")

def dfs(start):                                             # 노말한 dfs
    s = []
    s.append(start)
    visited[start] = True
    while s:
        start = s.pop()                                    # 도착은 99 시작은 0으로 고정
        if start == 99:                                    # 여기서 바로 변화하는 start가 목표치인 end가 되면 바로 1
            return 1

        for w in lst[start]:
            # print(w)
            if not visited[w]:
                s.append(w)
                visited[w] = True
    return 0                                                # 끝까지 같은 값이 안나오면 0 리턴

for tc in range(10):                                # 총 테스트케이스 10개
    T, line = map(int, input().split())             # T = 테스트케이스 번호 line = 줄의 갯수
    arr = list(map(int, input().split()))           # arr = 경로들 총 집합
    # print(arr)
    # print(T, N)

    visited = [0] * 100                             # visited 를 100개 빈공간 만들어주기
    lst = [[] for _ in range(line)]                 # 값을 넣을 lst를 마구 만들어주기
    idxlst = []                                     # 늘어놓은 값에서 짝수인덱스 값들만 모아놓기
    vallst = []                                     # 늘어놓은 값에서 홀수인덱스 값들만 모아놓기
    for i in range(len(arr)) :                      # arr의 길이만큼 돌려서 짝수와 홀수 인덱스에 해당하는걸 뽑기
        if i % 2 == 0 :
            idxlst.append(arr[i])
        else :
            vallst.append(arr[i])

    # print(idxlst)
    # print(vallst)
    for j in range(len(idxlst)) :                   # 어차피 2개가 한쌍이라서 len(arr)의 반값씩임
        lst[idxlst[j]].append(vallst[j])               # 빈lst의 idx[j]값에 해당하는 idx에 vallst[j]값을 넣어줌

    # print(lst)






    print(f'#{T} {dfs(1)}')