
def step1(strV) :
    ST = []
    postOrder = []
    isp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
    icp = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, ')' : 3}
    for token in strV :
        if token 이 숫자일때 :
            postOrder.append(token)
        elif ')' :
            ST에 왼쪽 괄호가 나올때까지 pop해서 postOrder에 추가

        else :
            if 스ㅐㄱ에 데이타 없는 경우 :
                ST에 token push
            elif isp(ST[-1]) < icp(token) :
                ST에 token을 push

            else:
                while token보다 크거나 같은 동안 :
                    pop해서 postOrder에 넣고
                    스탯에 token을 push

    while 스택에 데이타 있는 동안 :
        pop해서 postOrder에 넣는다.

    return postOrder


def step2(postOrder):
    ST = []

    for token in postOrder :
        if token이 숫자일때 :
            ST에 token push

        elif '+' :
            ST에서 두개 pop해서 더하기 연산
            연산 결과를 ST에 push
        elif '*' :

    return ST[-1]