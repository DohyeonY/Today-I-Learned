# 데이터 구조 복습 및 심화 예제 2

def group_anagrams(lst):
    dict = {}
    for w in lst:
        # print(w)
        t = ''.join(sorted(w))
    
        if t in dict:
            dict[t].append(w)
        else:
            dict[t] = [w]
    print(list(dict.values()))

group_anagrams(['eat','tea','tan','ate','nat','bat'])