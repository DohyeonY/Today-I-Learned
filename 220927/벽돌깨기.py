def break_block(col) :
    row = col의 첫번째 block의 위치를 찾아서
    lst = []
    lst.append((now , col))
    while lst :
        now, col = lst.pop(0)
        size = arr[row][col]
        for i in size :
            for d in 4개의 방향 :
                newX, newY
                if 범위 안에 있으면 :
                    lst.append((newY, newX))
                    arr[newY][newX] = 0

def drop(k) :
    if k == N :
        return

    for i in range(W) :
        backup = N단계의 arr
        break_block(i)

