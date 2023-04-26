import sys
sys.stdin=open("calcul.txt", "r")

def step1(strV):
    ST = []
    postOrder = []
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, ')': 3}

    for token in strV :
        # if 토큰이 숫자일때
        if token.isdigit() :                                # 숫자일때 바로 push
            postOrder.append(token)

        elif token == ')' :
            while ST[-1] != '(' :
                postOrder.append(ST.pop())
            ST.pop()

        elif token == '(' :  # ( 이면 스택에 ( push
            ST.append('(')

        elif not ST:
            ST.append(token)

        elif token == '+' or token == '*' :
            while isp[ST[-1]] >= icp[token]:  # 자기보다 낮은 연산자를 만날때까지
                postOrder.append(ST.pop())
            ST.append(token)


    while ST :
        postOrder.append(ST.pop())
    return ''.join(postOrder)


def step2(postOrder):
    ST = []
    for token in postOrder:
        # if token이 숫자일때 :
        if token.isdigit() :                      # 피연산자가 나오면 push
            # ST에 token push
            ST.append(token)

        elif token == '+' and len(ST) >= 2 :             # +이고 ST에 피연산자가 2개 이상 남아있으면
            # ST에서 두개 pop해서 더하기 연산
            a = int(ST.pop())
            b = int(ST.pop())
            # 연산 결과를 ST에 push
            ST.append(a + b)

        elif token == '*' and len(ST) >= 2 :             # *이고 ST에 피연산자가 2개 이상 남아있으면
            a = int(ST.pop())
            b = int(ST.pop())
            # 연산 결과를 ST에 push
            ST.append(a * b)

        elif token == '-' and len(ST) >= 2 :             # -이고 ST에 피연산자가 2개 이상 남아있으면
            a = int(ST.pop())
            b = int(ST.pop())
            # 연산 결과를 ST에 push
            ST.append(b - a)

        elif token == '/' and len(ST) >= 2 :             # /이고 ST에 피연산자가 2개 이상 남아있으면
            a = int(ST.pop())
            b = int(ST.pop())
            # 연산 결과를 ST에 push
            ST.append(b // a)


    return ST[0]

T = 10

for tc in range(1, T + 1):
    N = int(input())
    lst = input()
    a = step1(lst)
    b = step2(a)
    # print(b)


    print(f'#{tc} {b}')