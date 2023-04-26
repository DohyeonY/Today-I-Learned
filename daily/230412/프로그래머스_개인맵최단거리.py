from collections import deque
def bfs(maps,x,y):
    queue=deque()
    xy=[(-1,0),(1,0),(0,-1),(0,1)]
    max_maps = [[0] * len(maps[0]) for _ in range(len(maps))]

    queue.append((x,y))
    max_maps[x][y]=1
    while queue:
        x,y = queue.popleft()
        if x==len(maps) and y==len(maps[0]):
            break
        for i in range(len(xy)):
            nx = x+xy[i][0]
            ny = y+xy[i][1]

            if (nx>=0) and (ny>=0) and (nx<len(maps)) and (ny<len(maps[0])):
                if (maps[x][y]==1 and max_maps[nx][ny]==0):
                    queue.append((nx,ny))
                    max_maps[nx][ny] = max_maps[x][y] + 1

    return max_maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    if not bfs(maps,0,0):
        return -1
    return bfs(maps,0,0)