from this import d


N = 10
Q = [-1] * N
front = rear = -1

def enqueue(item) :
    global rear
    rear = rear + 1
    Q[rear] = item
    
def dequeue():
    global front
    front = front + 1
    return Q[front]