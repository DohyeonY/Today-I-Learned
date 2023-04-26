import sys
sys.stdin=open("turn.txt", "r")

def enqueue(item):                                           # push
    global rear
    rear = (rear + 1) % len(Q)
    Q[rear] = item

def dequeue():                                               # pop
    global front
    front = (front + 1) % len(Q)
    return Q[front]

T = int(input())
for tc in range(1, T+1) :
    # Q = [-1] * 21
    front = rear = -1
    N, M = map(int, input().split())
    Q = list(map(int,input().split()))
    # Q.append(queue)
    # print(Q)

    for _ in range(M) :
        enqueue(dequeue())


    print(f'#{tc} {dequeue()}')