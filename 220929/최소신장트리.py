# import sys
# sys.stdin=open("최소신장트리.txt", "r")

def find(x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for tc in range(1, T+1) :
    V, E = map(int, input().split())
    arr = []
    for _ in range(E) :
        n1, n2, cost = map(int, input().split())
        arr.append((cost, n1, n2))
    arr.sort()

    #print(arr)
    parent = [0] * (V + 1)
    costcnt = 0
    for i in range(1, V+1) :
        parent[i] = i
    #print(parent)
    for i in range(len(arr)) :
        cost, n1, n2 = arr[i]
        if find(n1) != find(n2) :
            union(n1, n2)
            costcnt += cost

    print(f'#{tc} {costcnt}')