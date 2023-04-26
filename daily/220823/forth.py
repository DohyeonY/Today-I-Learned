import sys
sys.stdin=open("forth.txt", "r")

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

        elif token == '.' :                              # . 가 나오면 ST에 남은 값을 return
            if len(ST) == 1 :                            # 그러나 값이 2개 남으면 error
                return ST[0]
            else:
                return 'error'
        else :                                           # 연산자가 나왔는데 피연산자의 갯수가 1이하면 에러 리턴
            return 'error'

T = int(input())

for tc in range(1, T + 1):
    N = input().split()
    result = step2(N)
    print(f'#{tc} {result}')
