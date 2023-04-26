# 크롤링을 통한 서비스 개발 예제4

blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

def blood_count(bl):

    bldic = {'A' : 0, 'B' : 0, 'AB' : 0, 'O' : 0}

    for blood in blood_types:
        # print(blood)
        bldic[blood] += 1
    
    return bldic



print(blood_count(blood_types))