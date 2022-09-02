import sys
sys.stdin=open("nodedis.txt", "r")

def BFS(arr, S, G, V) :                     # 그래프, 시작점, 정점의 갯수
    visited = [0] * (V + 1)
    Q = []                               # Q생성
    Q.append(S)                          # 시작점 S를 큐에 삽입
    visited[S] = 1
    while Q :                            # Q가 안비어 있으면
        t = Q.pop(0)                     # Q의 첫번째 원소 반환
        # visit
        for i in arr[t] :                # t와 연결된 모든 정점에 대해
            if not visited[i] :          # 방문되지 않은 곳이면
                Q.append(i)              # Q에 넣기
                visited[i] = visited[t] + 1 # t로부터 1만큼 이동
                if i == G :
                    return visited[G] -1    # 1부터 시작이니 -1
    # 못간다면 0
    return 0

T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())    # V = 노드의 갯수 E = 간선의 갯수
    arr = [[] for _ in range(V + 1)]    # 간선들
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())    # S = 스타트지점   G = 완료 지점
    # print(S, G)
    # print(arr)

    print(f'#{tc} {BFS(arr, S, G, V)}')