# 크롤링을 통한 서비스 개발 예제3
# count_vowels('apple') #=> 2
# count_vowels('banana') #=> 3
def count_vowels(int_lst) :

    result = int_lst.count('a') + int_lst.count('e') + int_lst.count('u') + int_lst.count('i') + int_lst.count('o')

    return result

print(count_vowels('banana'))
print(count_vowels('apple'))

