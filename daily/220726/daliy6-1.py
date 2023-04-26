# 크롤링을 통한 서비스 개발 예제

def de_identify(jumin):
    a = jumin[:6] + '*******'
    return a

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))

