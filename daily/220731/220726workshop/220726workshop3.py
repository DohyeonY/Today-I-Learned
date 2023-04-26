# 2. 솔로 천국 만들기

def lonely(a):

    lst = [a[0]]

    for i in a:

        if i != lst[-1]:
            lst.append(i)
            
    return lst

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))