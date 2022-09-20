import sys
sys.stdin=open("단순2진암호코드.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]


    # 1이 들어가있는 줄 찾기고 arr의 범위 줄이기
    a = -1
    for i in range(N) :
        if '1' in arr[i] :
            a = i
            break
    arr = arr[a]

    # 마지막에 1이 나오는곳을 찾기 위해 리스트화 해주고
    lst = []
    for i in arr :
        lst.append(i)

    # 마지막 좌표를 찾아줌
    endone = M
    for i in range(M-1, -1, -1) :
        if lst[i] == '1' :
            endone = i
            break

    # 마지막 좌표를 바탕으로 암호의 숫자는 56자이기 때문에 암호부분만 추출
    lst = lst[endone - 56 + 1 : endone + 1]

    aa = ''
    bb = ''
    cc = ''
    dd = ''
    ee = ''
    ff = ''
    gg = ''
    hh = ''

    # 각 암호를 분리해줌
    a = lst[0:7]
    b = lst[7:14]
    c = lst[14:21]
    d = lst[21:28]
    e = lst[28:35]
    f = lst[35:42]
    g = lst[42:49]
    h = lst[49:56]

    # 암호를 다시 넣어줌
    for i in a :
        aa += i
    for i in b :
        bb += i
    for i in c :
        cc += i
    for i in d :
        dd += i
    for i in e :
        ee += i
    for i in h :
        hh += i
    for i in f :
        ff += i
    for i in g :
        gg += i

    # 그걸 리스트에 넣어줌
    finallst = []
    finallst.append(aa)
    finallst.append(bb)
    finallst.append(cc)
    finallst.append(dd)
    finallst.append(ee)
    finallst.append(ff)
    finallst.append(gg)
    finallst.append(hh)

    # 암호표를 보고 맞으면 정수로 바꿔줌
    for i in range(8) :
        if finallst[i] == '0001101' :
            finallst[i] = 0
        elif finallst[i] == '0011001' :
            finallst[i] = 1
        elif finallst[i] == '0010011' :
            finallst[i] = 2
        elif finallst[i] == '0111101' :
            finallst[i] = 3
        elif finallst[i] == '0100011' :
            finallst[i] = 4
        elif finallst[i] == '0110001' :
            finallst[i] = 5
        elif finallst[i] == '0101111' :
            finallst[i] = 6
        elif finallst[i] == '0111011' :
            finallst[i] = 7
        elif finallst[i] == '0110111' :
            finallst[i] = 8
        elif finallst[i] == '0001011' :
            finallst[i] = 9

    # 유효한 암호인지 확인하려 홀수번째와 짝수번째를 각각 처리해줌
    result = ((finallst[0] + finallst[2] + finallst[4] + finallst[6]) * 3) + (finallst[1] + finallst[3] + finallst[5] + finallst[7])

    # 만약 10의 배수이면 다 더해주고
    if result % 10 == 0 :
        result = 0
        for i in range(8) :
            result += finallst[i]
    # 아니면 0
    else :
        result = 0
    print(f'#{tc} {result}')


