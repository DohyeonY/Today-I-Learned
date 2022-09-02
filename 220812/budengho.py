def budengho(str1, str2) :

    if str1 == str2 :
        return 0
    elif str1 < str2 :
        return -1
    else :
        return 1

print(budengho('abcd', 'b'))
print(budengho('b', 'abcd'))
print(budengho('abcd', 'abcd'))
