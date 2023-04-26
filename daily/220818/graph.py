import sys

sys.stdin = open("graph.txt", "r")


def dfs(start):                                             # 노말한 dfs
    s = []
    s.append(start)
    visited[start] = True
    while s:
        start = s.pop()
        if start == end:                                    # 여기서 바로 변화하는 start가 목표치인 end가 되면 바로 1
            return 1

        for w in lst[start]:
            # print(w)
            if not visited[w]:
                s.append(w)
                visited[w] = True
    return 0                                                # 끝까지 같은 값이 안나오면 0 리턴


T = int(input())                                            # testcase

for tc in range(1, T + 1):
    # SG = []

    V, E = map(int, input().split())                        # V = 노드의 갯수, E = 줄의 갯수
    visited = [False for _ in range(V+1)]                   # visited 선언
    # print(visited)
    # for _ in range(V+1) :
    lst = [[0] * (V+1) for _ in range(V+1)]                 # 빈 lst를 노드 갯수 +1개 만큼 만들어줌 이유는 인덱스 0은 [] 로 남기기위해
    for _ in range(E) :                                     # S = 출발노드 G = 도착노드
        S, G = map(int, input().split())
        lst[S].append(G)                                    # 빈 리스트의 S인덱스에 G도착노드를 넣어 준다
    # print(S, G)

    # lst.append(arr)
    # print(f'#{tc} {arr}')
    start, end = map(int, input().split())                  # start = 문제의 출발지점 end = 문제의 목표지점


    print(f'#{tc} {dfs(start)}')
    # print(start, end)
