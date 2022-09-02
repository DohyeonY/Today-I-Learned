# 1. 무엇이 중복일까

def duplicated_letters(a):
    
    duplicated = []

    for i in a :

        if a.count(i) > 1 and i not in duplicated:
            duplicated.append(i)

    return duplicated


print(duplicated_letters("apple"))
print(duplicated_letters("banana"))