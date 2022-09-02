def chage(num) :
    if swich[num] == 1 :
        swich[num] = 0
    else :
        swich[num] = 1

    return

swich_num = int(input())

swich = [-1] + list(map(int, input().split()))
student_num = int(input())
for _ in range(student_num) :
    sex, num = map(int, input().split())
    # 남자일때
    if sex == 1 :
        for i in range(num, swich_num+ 1, num) :
            chage(i)


    # 여자일때
    else :
        chage(num)
        for k in range(swich_num//2) :
            if num + k > swich_num or num - k < 1 :
                break
            if swich[num + k] == swich[num - k] :
                chage(num + k)
                chage(num - k)

            else :
                break

result = []
for i in range(1, len(swich)) :

    print(swich[i], end=' ')
    if i % 20 == 0 :
        print()

