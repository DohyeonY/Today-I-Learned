import sys
sys.stdin=open("pizza.txt", "r")

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

T = int(input())
T = 1
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    Pizza = list(map(int, input().split()))
    Q = []
    front = rear = -1

    enqueue(Pizza)
    dequeue()
    # print(N, M)
    # print(Pizza)
    for i in range(N) :
        enqueue(Pizza[i] // 2)
        if Q[i] != 0 :     # Q[i] != 0일때
            Q[i] = Q[i] // 2
        else :          # Q[i] == 0일때
            enqueue(Q[i])


    print(Q)