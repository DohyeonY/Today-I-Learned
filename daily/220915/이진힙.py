import sys
sys.stdin=open("이진힙.txt", "r")

# 삽입
def insert(data):
    # [0]인 힙의 0 뒷부분부터 데이터 차곡차곡
    heap.append(data)
    # 앞에 0이 있으니 힙의 길이 -1 이 자신의 인덱스
    index = len(heap) - 1
    # 인덱스가 1보다크고 부모보다 작을때 계속 진행
    while index > 1 and heap[index] < heap[index // 2]:
        # 부모랑 자식 바꿔주기
        heap[index], heap[index // 2] = heap[index // 2], heap[index]
        # 부모랑 자식이 바뀌었으니 부모의 인덱스값을 부모의 값으로 바꿔줌
        index //= 2

# 마지막으로 들어간 녀석의 부모들을 다 더해주기
def sum_parents():
    value = 0
    # 마지막 노드의 조상노드를 시작점으로 지정
    idx = N // 2
    while idx:
        # 밸류에 저장
        value += heap[idx]
        # 부모 노드로 이동
        idx //= 2
    return value

# testcase
T = int(input())
for tc in range(1, T+1) :
    # 노드의 갯수
    N = int(input())
    # 정수들이 순서대로 입력
    lst = list(map(int, input().split()))

    heap = [0]
    for data in lst :
        insert(data)
    answer = sum_parents()

    print(f'#{tc} {answer}')