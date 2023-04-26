import sys
sys.stdin=open("q1.txt", "r")

def isEmpty():                                               # q가 비었는지 확인
    return front == rear

def isFull():                                                # q가 꽉찼는지 확인
    return front == (rear + 1) % len(q)

def enqueue(item):                                           # push
    global rear
    rear = (rear + 1) % len(Q)
    Q[rear] = item

def dequeue():                                               # pop
    global front
    front = (front + 1) % len(Q)
    return Q[front]

qsize = 9
Q = [0] * qsize
front = rear = 0
for tc in range(1, 11):
    T = int(input())
    lst = list(map(int, input().split()))
    for i in lst:
        enqueue(i)

    cnt = 1                                                  # 1~5까지 빼주기 위한 cnt
    while Q[rear]:                                           # 큐에 데이터가 있는 동안
        i = dequeue() - cnt                                  # i에 cnt만큼 빼준다
        cnt += 1                                             # 사이클을 돌리기 위해 cnt에 1씩 더해줌
        if cnt == 6:                                         # 1~5까지만 돌려야하기에 cnt가 6이 되면 1로 초기화
            cnt = 1
        if i < 0:                                            # 만약 i가 0보다 작아지면 0으로 바꿔서 while문을 종료
            i = 0
        enqueue(i)                                           # 그게 아니라면 cnt빼주고 다시 enqueue시켜줌
    print(f'#{tc}', end=' ')
    while not isEmpty():                                     # rear와 front가 같아질때까지 dequeue시켜줌
        print(dequeue(), end=' ')
    print()
