# 2. 소대소대

def low_and_up(a):
    
    loup = ""
    a = a.upper()

    for i in range(len(a)) :

        if i % 2 == 0 :
            loup += a[i].lower()

        else : loup += a[i]

    return loup
#         if a.count(i) > 1 and i not in duplicated:
#             loup.append(i)

#     return loup


print(low_and_up("apple"))
print(low_and_up("banana"))