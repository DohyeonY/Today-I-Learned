from collections import deque
import sys
sys.stdin = open('연산.txt')

def bfs(N) :
    global result
    Q = deque()
    Q.append((N, 0))

    while Q :
        Num, Cnt = Q.popleft()

        if Num == M :
            if result > Cnt :
                result = Cnt
                return

        lst = [Num+1, Num-1, Num*2, Num-10]
        for i in lst :
            if i not in visited and i > 0 and i <= 1000000 :
                visited.add(i)
                Q.append((i, Cnt + 1))

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    visited = set()
    result = 99999999999
    bfs(N)
    print(f'#{tc} {result}')