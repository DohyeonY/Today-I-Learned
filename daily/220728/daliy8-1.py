# OOP의 상속과 오버라이딩 예제 1
participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
a = sorted(participants)
# print(a)
result = 0
for i in range(len(a)) :
    # print(i)
    if a[i] == a[i-1] or a[i-1] == a[i] :
        continue
    else :
        result = a[i]

print(result)