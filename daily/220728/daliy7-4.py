# OOP의 메서드에 대한 이해와 사...

def fee(time, dis) :
    result = 0
    
    result += (time / 10) * 1200

    if time % 60 >= 50 :
        result += ((time // 30) + 1) * 525

    else :
        result += (time // 30) * 525

    if dis > 100 :
        result += (100 * 170) + (dis - 100) * 85

    else :
        result += dis * 170

    return result

print(round(fee(600,50)))