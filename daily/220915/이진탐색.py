import sys
sys.stdin=open("이진탐색.txt", "r")

# 중위 순회
def inorder(node):
    global cnt

    if node <= N:
        inorder(node * 2)   # 왼쪽 노드
        arr[node] = cnt    # 왼쪽 다 다녀 왔으면 값 넣어
        cnt += 1           # 값 하나 추가
        inorder((node * 2) + 1) # 오른쪽 노드


T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 이진 탐색 트리에 저장할 노드 개수

    arr = [0] * (N + 1)     # N+1로 만들어 주기

    cnt = 1       # 0 말구 1부터 시작
    inorder(1)    # 중위순회 하면 오름차순으로 정렬된 값을 얻을 수 있다.

    print(f'#{tc} {arr[1]} {arr[N//2]}')
