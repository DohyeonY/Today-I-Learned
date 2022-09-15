import sys
sys.stdin=open("노드의합.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())  # N:노드개수, M:리드노프개수, L:출력할 노드번호
    arr = [0 for _ in range(N + 1)]
    # print(arr)
    for i in range(M):
        node, value = map(int, input().split()) # 노드번호와 값 받기
        arr[node] = value
    # print(arr)

    for i in range(N, 0, -1):
        if i // 2 > 0:
            arr[i // 2] += arr[i]

    print(f"#{tc} {arr[L]}")        # 출력할 노드 번호에 맞는 arr출력