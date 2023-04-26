ARR = [[] for _ in range()]
for row in range(...) :
    for col in range(...) :
        if col == 0 or 마지막 거면 :
            ARR(row).append(1)
        else :
            ARR(row).append(ARR[row-1][col-1] + ARR[row-1][col-1])