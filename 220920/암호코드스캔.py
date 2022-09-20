import sys
sys.stdin=open("암호코드스캔.txt", "r")

dict_16 = {'0': '0000', '1': '0001',
           '2': '0010', '3': '0011',
           '4': '0100', '5': '0101',
           '6': '0110', '7': '0111',
           '8': '1000', '9': '1001',
           'A': '1010', 'B': '1011',
           'C': '1100', 'D': '1101',
           'E': '1110', 'F': '1111'}

dict_code = {(2, 1, 1) : 0,
             (2, 2, 1) : 1,
             (1, 2, 2) : 2,
             (4, 1, 1) : 3,
             (1, 3, 2) : 4,
             (2, 3, 1) : 5,
             (1, 1, 4) : 6,
             (3, 1, 2) : 7,
             (2, 1, 3) : 8,
             (1, 1, 2) : 9}

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = sorted(list(set([input()[:M] for _ in range(N)])))
    final = 0
    visited = []
    arr.pop(0)
    # print(arr)
    for i in range(len(arr)) :
        code = ''
        for j in range(len(arr[i])) :
            code += dict_16[arr[i][j]]
        code = code.rstrip("0")

        lst = []
        r1 = r2 = r3 = r4 = 0
        for i in range(len(code)-1, -1, -1) :
            if code[i] == '1' and r3 == 0 :
                r4 += 1
            elif code[i] == '0' and r2 == 0 :
                r3 += 1
            elif code[i] == '1' and r1 == 0 :
                r2 += 1
            elif code[i] == '0' :
                if code[i-1] == '1' :
                    j = min(r2, r3, r4)
                    lst.append((dict_code[r2 // j, r3 // j, r4 // j]))
                    r2 = r3 = r4 = 0
                    if len(lst) == 8 :
                        if not ((lst[1] + lst[3] + lst[5] + lst[7]) * 3 + lst[0] + lst[2] + lst[4] + lst[6]) % 10 :
                            if lst not in visited :
                                final += sum(lst)
                                visited.append(lst)
                        lst = []
    print(f'#{tc} {final}')
    #     code = code.rstrip('0')
    #     print(code)
    #     r1 = r2 = r3 = 0

    #     arr = arr.replace('0', '0000')
    #     arr = arr.replace('1', '0001')
    #     arr = arr.replace('2', '0010')
    #     arr = arr.replace('3', '0011')
    #     arr = arr.replace('4', '0100')
    #     arr = arr.replace('5', '0101')
    #     arr = arr.replace('6', '0110')
    #     arr = arr.replace('7', '0111')
    #     arr = arr.replace('8', '1000')
    #     arr = arr.replace('9', '1001')
    #     arr = arr.replace('A', '1010')
    #     arr = arr.replace('B', '1011')
    #     arr = arr.replace('C', '1100')
    #     arr = arr.replace('D', '1101')
    #     arr = arr.replace('E', '1110')
    #     arr = arr.replace('F', '1111')
    # print(arr)
    # length = 4
    # newarr = [''.join(x) for x in zip(*[list(arr[z::length]) for z in range(length)])]
    # arr = map(''.join, zip(*[iter(arr)] * length))
    # print(newarr)
    # lst = []
    # for i in newarr :
    #     if i == '0000' :
    #         i = '0'
    #         lst.append(i)
    #     elif i == '0001' :
    #         i = '1'
    #         lst.append(i)
    #     elif i == '0010' :
    #         i = '2'
    #         lst.append(i)
    #     elif i == '0011' :
    #         i = '3'
    #         lst.append(i)
    #     elif i == '0100' :
    #         i = '4'
    #         lst.append(i)
    #     elif i == '0101' :
    #         i = '5'
    #         lst.append(i)
    #     elif i == '0110' :
    #         i = '6'
    #         lst.append(i)
    #     elif i == '0111' :
    #         i = '7'
    #         lst.append(i)
    #     elif i == '1000' :
    #         i = '8'
    #         lst.append(i)
    #     elif i == '1001' :
    #         i = '9'
    #         lst.append(i)
    #     elif i == '1010' :
    #         i = '10'
    #         lst.append(i)
    #     elif i == '1011' :
    #         i = '11'
    #         lst.append(i)
    #     elif i == '1100' :
    #         i = '12'
    #         lst.append(i)
    #     elif i == '1101' :
    #         i = '13'
    #         lst.append(i)
    #     elif i == '1110' :
    #         i = '14'
    #         lst.append(i)
    #     elif i == '1111' :
    #         i = '15'
    #         lst.append(i)
    # # print(lst)
    # odd = 0
    # even = 0
    # for i in range(0, len(lst), 2) :
    #     odd += int(lst[i])
    # for i in range(1, len(lst), 2) :
    #     even += int(lst[i])
    #
    # result = 0
    # result = (odd * 3) + even
    # if result % 10 != 0 :
    #     result = 0
    #     print(f'#{tc} {result}')
    #
    # else :
    #     result = odd + result
    #     print(f'#{tc} {result}')


#     newarr = []
#     for row in range(1, N) :
#         j = M * 4 - 1
#
#         while j >= 56 :
#             if newarr[row][j] == 1 and newarr[row - 1][j] == 0 :
#                 for i in range(8) :
#                     a[2] = 1의 갯수를 셈
#                     a[1] = 0의 갯수를 셈
#                     a[0] = 1의 갯수를 셈
#                     k = min(a[0:2])
#
#                     코드하나를 찾아온다.
#
#                 암호검증
#
#             else :
#                 j -= 1
#
# 111011011000101110110110001011000100011010010011011110000111011011
# 00010111011011000101100010001101001001101111