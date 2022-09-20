import sys
sys.stdin=open("이진수.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, six = input().split()

    # print(N, six)
    s = str(six)

    # print(s)
    s = s.replace('0', '0000')
    s = s.replace('1', '0001')
    s = s.replace('2', '0010')
    s = s.replace('3', '0011')
    s = s.replace('4', '0100')
    s = s.replace('5', '0101')
    s = s.replace('6', '0110')
    s = s.replace('7', '0111')
    s = s.replace('8', '1000')
    s = s.replace('9', '1001')
    s = s.replace('A', '1010')
    s = s.replace('B', '1011')
    s = s.replace('C', '1100')
    s = s.replace('D', '1101')
    s = s.replace('E', '1110')
    s = s.replace('F', '1111')

    print(f'#{tc} {s}')




