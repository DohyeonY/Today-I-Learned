import sys
sys.stdin=open("중위순회.txt", "r")

def pre(root) :                                                         # 중위순회 함수
    if root :    # root != 0 :
        pre(tree[root][1])
        print(tree[root][0], end='')
        pre(tree[root][2])

T = 10

for tc in range(1, T+1) :
    N = int(input())                                                   # 글자수
    tree = [[0, 0, 0] for _ in range(N+1)]                             # 빈 tree
    lst = [list(map(str, input().split())) for _ in range(N)]


    # parent = [0] * (101)
    # print(lst)
    # #2. [[] for _] 의 형태로 만들어 놓은 경우 [[], []...]
    for i in range(N) :
        tree[int(lst[i][0])][0] = lst[i][1]                            # tree에 lst 요소 넣어주기
        if len(lst[i]) == 3 :                                          # 1개만 있을때
            tree[int(lst[i][0])][1] = int(lst[i][2])
        elif len(lst[i]) == 4 :                                        # 2개 있을때
            tree[int(lst[i][0])][1] = int(lst[i][2])
            tree[int(lst[i][0])][2] = int(lst[i][3])
    print('#', end='')
    print(tc, end=' ')
    pre(1)
    print()
    # print(lst)
    # print(tree)
#
# a = ['1', 'A', '2', '3']
# a = ['1', 'A', '2']
# a = ['1', 'A']
# # 초기에 tree를 만들어 놓은  경우 [[0,0,0], ...]
# for i in range(1, len(a)) :
#     tree[int(a[0])] = a[i]
# #2. [[] for _] 의 형태로 만들어 놓은 경우 [[], []...]
# for i in range(1, len(a)) :
#     tree[int(a[0])].append(a[i])
# #3. #2나 일차원 배열로 만드어 놓은 경우 []
# tree[int(a[0])] = a[1:len(a)]
