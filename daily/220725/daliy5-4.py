# 요청과 응답에 따른 데이터 수집
def sum_of_repeat_number(suml) :

    sum = 0

    for i in suml :

        if suml.count(i) != 1 :
            continue
        else :
            sum += i

    return sum

suml = [4,4,7,8,10,4]
print(sum_of_repeat_number(suml))
            