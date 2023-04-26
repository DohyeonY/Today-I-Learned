import sys
sys.stdin=open("calcul.txt", "r")


isp = {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
icp = {')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '(': 3}


def asd(arr):
    st = []
    result = []
    for i in arr:
        # i가 숫자면
        if '0' <= i <= '9':
            # result에 넣고
            result.append(i)
        # 닫는 괄호면
        elif i == ')':
            # 여는 괄호를 만날때까지 result.append(st.pop())
            while st[-1] != '(':
                result.append(st.pop())
            # 남아있는 여는 괄호 pop
            st.pop()
        # i가 숫자가 아닐때
        else:
            # st이 비어있으면 어펜드 i
            if not st:
                st.append(i)
            # st에 값이 있을때
            elif st:
                # 들어오는 i가 st의 마지막 값보다 작으면
                if icp[i] <= isp[st[-1]]:
                    # result에 st.pop해서 넣음
                    result.append(st.pop())
                    # 들어온 i를 st에 넣음
                    st.append(i)
                # 들어오는 i가 st의 마지막 값보다 크면
                else:
                    # 걍 넣음
                    st.append(i)
    # 스텍에 값이 남아있으면
    if st:
        # 리졀트에 st을 팝해서 넣음
        result.append(st.pop())
    return ''.join(result)


def dsa(result1):
    st = []
    for i in result1:
        # i가 숫자면
        if str.isdigit(i):
            # st에 숫자형으로 변환해서 넣음
            st.append(int(i))
        else:
            if i == '+':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 + op2)
            elif i == '*':
                op2 = st.pop()
                op1 = st.pop()
                st.append(op1 * op2)
    return st.pop()


T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = input()

    result1 = asd(arr)
    result = dsa(result1)
    print(result1)
    # print(f'#{tc} {result}')