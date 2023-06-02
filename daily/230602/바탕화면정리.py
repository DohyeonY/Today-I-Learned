def solution(wallpaper):
    # print(wallpaper)
    column = []
    row = []
    
    for i in range(len(wallpaper)) :
        for j in range(len(wallpaper[i])) : 
            # print(j)
            if wallpaper[i][j] == "#": 
                column.append(i)
                row.append(j) 

    return [min(column), min(row), max(column) + 1, max(row) + 1]