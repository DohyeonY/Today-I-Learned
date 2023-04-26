import sys
sys.stdin=open("checking.txt", "r")

T = int(input())                            # testcase
# result = 0
for tc in range(1, T+1) :
    arr = input()                          # 입력받기
    # print(arr)
    stack = []                             # (){}를 받는 스택

    result = 1
    # print(len(stack1))

    for i in arr :                          # 입력받은 문장을 검사
        # print(i)
        if len(stack) == 0 :                # 스택이 비어있을때 } ) 가 나오면 그냥 바로 result는 0
            if i == '}' or i == ')' :
                result = 0
                break
            elif i =='{' or i == '(' :      # { (가 나오면 그냥 넣기
                stack.append(i)

        else :                  # 값이 있을때
            if stack[-1] == '(' and i == ')' :      # 이전 값과 i값이 () 짝을 이루면 pop
                stack.pop()
                continue
            elif stack[-1] == '{' and i == '}' :    # 이전 값과 i값이 {} 짝을 이루면 pop
                stack.pop()
                continue
            elif i == '(' or i == '{' :             # {( 값이 나오면 push
                stack.append(i)
            elif i == ')' or i == '}' :             # 값이 있을때 짝이 안맞는 닫는게 나오면 바로 result=0
                result = 0
                break

    if stack :                                      # 만약 스택에 값이 남아있으면 걍 result = 0
        # print(stack)
        result = 0

    print(f'#{tc} {result}')








    #
    #     if i == '(' :                       # (가 뜨면 push
    #         stack1.append('(')
    #
    #     if i == ')' :                       # )가 뜨면 pop
    #         stack1.pop()
    #
    #     if i == '{' :                       # {가 뜨면 push
    #         stack2.append('{')
    #
    #     if i == '}' :                       # }가 뜨면 pop
    #         stack2.pop()
    # print(stack1, stack2)
    # print(len(stack1), len(stack2))
    #
    # if len(stack1) == 0 and len(stack2) == 0 :   # stack들의 길이가 0이면 = 짝이 잘 맞으면 결과는 1
    #     result = 1
    # else :                                  # 아니면 0
    #     result = 0
    #
    # print(f'#{tc} {result}')