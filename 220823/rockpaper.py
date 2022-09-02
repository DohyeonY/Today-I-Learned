def winner(i, j) :
    if 영역의 데이터가 한개일때 :
        return 한개의 위치
    lw = winner(i, (i+j)//2)
    rw = winner((i+j)//2+1, j)
    if lw와 rw의 우승자를 결저하여 위치를 return