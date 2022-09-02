"""
재현이와 재민이는 장부를 관리하고 있음
빡통 재현이는 잘못된 수를 부를 때마다 0을 외쳐서
최근에 재민이가 쓴 수를 지우게 함(pop)
재민이는 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다.
재민이를 도와주자!

스택을 활용하면 된다.
0이 아닌 숫자를 입력한 것은 push로
0을 입력하면 pop으로 이전에 입력한 값을 지워버리면 해결 끝!
"""

def push(item) :            # push 함수
    ST.append(item)

    # global top
    # top += 1
    # if top == size :
    #     print('overflow!')
    # else :
    #     ST[top] = item


def pop() :                 # pop 함수
    if len(ST) == 0 :
        # print('underflow')
        return

    else :
        return ST.pop(-1)


K = int(input())            # 줄의 갯수
size = K                    # 스택의 크기를
ST = [0] * size             # K만큼 주기 위해서 사용
top = -1                    # top의 시작은 -1

for _ in range(K) :         # 입력 받을때 숫자 + 엔터로 받기 때문에 K번 만큼 돌려줘야함
    num = int(input())      # 입력
    if num >= 1 :           # 받는 숫자가 0이 아니면(1보다 크거나 같으면) 스택에 쌓아줌
        push(num)

    else :                  # 그게 아니면(0이면, 입력받는 정수의 범위가 0~100,000이라 -가 없음) 제거
        pop()

sumv = 0                    # sum 대체 함수
for i in range(len(ST)) :   # 이거 안쓰면 시간 초과 뜸 ;;
    sumv += ST[i]

print(ST)
