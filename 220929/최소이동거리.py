import sys
sys.stdin=open('최소이동거리.txt')


def dijkstra(start):
    dis[start] = 0

    # 노드의 개수만큼 반복
    for _ in range(N + 1):
        min_idx = -1
        min_value = float('inf')

        for i in range(N + 1):
            if not visited[i] and dis[i] < min_value:
                min_idx = i
                min_value = dis[i]

        visited[min_idx] = 1

        for i in range(N + 1):
            if mat[min_idx][i] and not visited[i]:
                dis[i] = min(dis[i], dis[min_idx] + mat[min_idx][i])


T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(E)]

    # 인접 행렬
    mat = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for s, e, w in arr:
        mat[s][e] = w

    visited = [0 for _ in range(N + 1)]
    dis = [float('inf') for _ in range(N + 1)]

    dijkstra(0)

    print(f'#{tc} {dis[N]}')



# T = int(input())
#
# for tc in range(1, T+1) :
#     N, E = map(int, input().split())
#     lst = []
#     for _ in range(E) :
#         lst.append(list(map(int, input().split())))
#     print(lst)
#

