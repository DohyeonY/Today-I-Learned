ST = []

def push(item) :
    ST.append(item)

def isEmpty() :
    if len(ST) > 0 :
        return True
    return False

def pop() :
    if len(ST) > 0 :
        ST.pop()


size = 100
ST = [' '] * size
top = -1

def isEmpty():
    if top > 0:
        return False
    return True

def isFull() :
    if top == size
