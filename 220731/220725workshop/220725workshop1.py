# 1. 평균 점수 구하기

# get_dict_avg({'python' : 80, 'web' : 83, 'algorithm' : 90, 'django' : 89})

def get_dict_avg(dic) :
    a = dic.values()
    b = 0
    c = 0
    for i in a :
        b += i
        c = b / len(a)
    print(c)


get_dict_avg({'python' : 80, 'web' : 83, 'algorithm' : 90, 'django' : 89})