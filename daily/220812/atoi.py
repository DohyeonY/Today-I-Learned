# def atoi(s) :
#     i = 0
#     for x in s :
#         i = i*10 + ord(x) - ord('0')
#     return i
#
# a = atoi('123')
# print(atoi('123'))
# print(a + 1)
# a = 123

def myStr(value):
    result = ''
    newV = value
    if newV < 0:
        newV = newV * -1

    while newV > 0:
        num = newV % 10
        tmp = chr(ord('0') + num)
        result = tmp + result
        newV = newV // 10

    if value < 0:
        result = '-' + result

    return result


print(myStr(123) + 'a')
print(myStr(321) + 'b')
print(myStr(-321) + 'c')
# print(chr(97))

