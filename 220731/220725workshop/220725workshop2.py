# 2. 혈액형 분류하기



def count_blood(blood_types) :

    dic = dict.fromkeys(blood_types,0)

    for blood_type in blood_types:

        dic[blood_type] += 1

    return dic

print(count_blood([ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']))