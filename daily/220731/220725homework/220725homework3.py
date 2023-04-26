# 3. 정사각형만 만들기



def only_square_area(a, b) :
    lst = []
    for aw in a :
        for bw in b :
            if aw == bw :
                lst.append(aw*bw)
    return lst
        # if i in only_square_area[1] :
            
print(only_square_area([32,55,63], [13,32,40,55]))