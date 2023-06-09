def solution(park, routes):
    direct = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
    
    x, y = 0, 0 
    n, m = len(park[0]), len(park) 
    
    maps = []
    for idx1, p1 in enumerate(park):
        map = []
        for idx2, p2 in enumerate(p1):
            if p2 == 'S':
                x = idx2
                y = idx1
            map.append(p2)
        maps.append(map)
        map = []
    
    for route in routes:
        d, num = route.split(' ')
        
        px, py = x, y
        for _ in range(int(num)):
            nx, ny = x + direct[d][1], y + direct[d][0]
            if (nx >= n or nx < 0) or (ny >= m or ny < 0) or (maps[ny][nx] == 'X'):
                x, y = px, py
                break
            else:
                x, y = nx, ny

    return [y, x]