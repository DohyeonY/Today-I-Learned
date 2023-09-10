from collections import deque

flag=0
answer=0

def solution(maps) :
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    
    def bfs(x, y) :
        global flag, answer
        visited=[[0] * len(maps[0]) for _ in range(len(maps))]
        visited[x][y] = 1
        dq = deque()
        dq.append((x, y))
        
        while dq:
            cx,cy=dq.popleft()
            for i in range(4) :
                nx, ny = cx + dx[i], cy + dy[i]
                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]) :
                    continue
                if (maps[nx][ny] == 'O' or maps[nx][ny] == 'S') and visited[nx][ny] == 0 :
                    visited[nx][ny] = visited[cx][cy] + 1
                    dq.append((nx,ny))
                elif maps[nx][ny] == 'L' and flag == 0 :
                    visited[nx][ny] = visited[cx][cy] + 1
                    labor = [nx, ny]
                    flag = 1
                    answer = visited[nx][ny] - 1
                    return labor
                elif maps[nx][ny] == 'E' and flag == 1 :
                    visited[nx][ny] = visited[cx][cy] + 1
                    end=[nx,ny]
                    answer += visited[nx][ny] - 1
                    return end
                elif maps[nx][ny] == 'L' and visited[nx][ny] == 0 and flag == 1 :
                    visited[nx][ny] = visited[cx][cy] + 1
                    dq.append((nx,ny))
                elif maps[nx][ny] == 'E' and visited[nx][ny] == 0 and flag == 0 :
                    visited[nx][ny] = visited[cx][cy] + 1
                    dq.append((nx,ny))
                    
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == 'S' :
                x = bfs(i, j)
                break
    if answer == 0 and flag == 0:
        return -1
    
    firstAns = answer
    
    x=bfs(x[0], x[1])
    
    if firstAns == answer :
        return -1
    
    return answer