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