import sys
sys.stdin=open("정식이의은행업무.txt", "r")

T = int(input())
twoj = ['0','1']
threej = ['0','1','2']

for tc in range(1, T+1) :
    jin2 = input()
    jin3 = input()
    # print(jin2, jin3)
    jin2save = []
    jin3save = []
    # 2진법에서 첫번째 숫자가 0이 될 수 없고 1만 가능하니 굳이 idx0은 변환하지 않음
    for i in range(1, len(jin2)):
        jin2lst = list(jin2)
        if jin2lst[i] == '0':
            jin2lst[i] = '1'
            jin2save.append(int(''.join(jin2lst), 2))
        else :
            jin2lst[i] = '0'
            jin2save.append(int(''.join(jin2lst), 2))

    # 3진수도 제일 앞에 0이 올수는 없으니까 0으로 변환할때는 조건을 붙여줌
    for i in range(len(jin3)) :
        jin3lst = list(jin3)
        if jin3lst[i] == '0' :
            jin3lst[i] = '1'
            jin3save.append(int(''.join(jin3lst), 3))
            jin3lst[i] = '2'
            jin3save.append(int(''.join(jin3lst), 3))
        elif jin3lst[i] == '1' :
            jin3lst[i] = '2'
            jin3save.append(int(''.join(jin3lst), 3))
            if i >= 1 :
                jin3lst[i] = '0'
                jin3save.append(int(''.join(jin3lst), 3))

        else :
            if i >= 1 :
                jin3lst[i] = '0'
                jin3save.append(int(''.join(jin3lst), 3))
            jin3lst[i] = '1'
            jin3save.append(int(''.join(jin3lst), 3))

    result = 0
    for i in jin2save :
        if i in jin3save :
            result = i
            break

    print(f'#{tc} {result}')

