import sys
sys.stdin=open("gns.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    test_case, N = input().split()
    lst = list(input().split())
    N = int(N)
    # print(lst[:5])
    relst = [0] * 10

    for i in range(len(lst)):

        if lst[i] == 'ZRO' :
            relst[0] += 1
        elif lst[i] == 'ONE' :
            relst[1] += 1
        elif lst[i] == 'TWO' :
            relst[2] += 1
        elif lst[i] == 'THR' :
            relst[3] += 1
        elif lst[i] == 'FOR' :
            relst[4] += 1
        elif lst[i] == 'FIV' :
            relst[5] += 1
        elif lst[i] == 'SIX' :
            relst[6] += 1
        elif lst[i] == 'SVN' :
            relst[7] += 1
        elif lst[i] == 'EGT' :
            relst[8] += 1
        else :
            relst[9] += 1

    # print(relst)

    print(test_case)
    print(('ZRO ' * relst[0]) + ('ONE ' * relst[1]) + ('TWO ' * relst[2]) + ('THR ' * relst[3]) + ('FOR ' * relst[4]) + ('FIV ' * relst[5]) + ('SIX ' * relst[6]) + ('SVN ' * relst[7]) + ('EGT ' * relst[8]) + ('NIN ' * relst[9]))
