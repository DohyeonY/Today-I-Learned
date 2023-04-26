lst = [9,4,8,7,6,5,1,3,2]

for j in range(len(lst)-1, 0, -1) :
    for i in range(j) :
        if lst[i] > lst[i+1] :
            lst[i], lst[i+1] = lst[i+1], lst[i]


print(lst)