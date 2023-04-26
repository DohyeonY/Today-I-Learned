inputS = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

def pre(root) :
    if root :    # root != 0 :
        print(root)
        pre(tree[root][1])
        pre(tree[root][2])


def pre1(root) :
    print(root)
    if tree[root][1] != 0 :
        pre(tree[root][1])
    if tree[root][2] != 0:
        pre(tree[root][2])


T = 10
for tc in range(1, T+1) :\
    N = int(input())
    lst = list(map(int, inputS.split()))
V = 13

# print(lst)
tree = [[0,0,0] for _ in range(V+1)]
parent = [0] * (V+1)
# print(tree)

for idx in range(0, len(lst), 2) :
    P, C = lst[idx], lst[idx+1]
    if tree[P][0] == 0 :
        tree[P][0] = C
    else :
        tree[P][1] = C
    parent[C] = P # 부모확인
# print(tree)
# print(parent)
pre(1)