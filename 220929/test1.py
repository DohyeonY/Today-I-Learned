# 특정 원소가 속한 집합을 찾기
def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    # if a < b:
    parent[b] = a
    # else:
    #     parent[a] = b

T = int(input())

for tc in range(1, T+1) :
# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
    N, M = map(int, input().split())
    parent = [0] * (N + 1) # 부모 테이블 초기화하기

    # 부모 테이블상에서, 부모를 자기 자신으로 초기화
    for i in range(1, N + 1):
        parent[i] = i
    arr = list(map(int, input().split()))

    # Union 연산을 각각 수행
    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i+1]
        union(a, b)
    # print(parent)
    cnt = 0
    result = set()
    for i in parent :
        result.add(find(i))
    # print(result)
    # print(parent)
    print(f'#{tc} {len(result)-1}')
    #
    # for i in range(1, N+1) :
    #     if i in parent :
    #         cnt += 1
    # print(f'#{tc} {cnt}')
