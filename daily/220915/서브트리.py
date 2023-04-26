import sys
sys.stdin=open("서브트리.txt", "r")
# 중위 순회 사용
def inorder(T):
    global count
    if T==0:
        return
    count+=1
    inorder(a1[T])
    inorder(a2[T])

# testcase
T=int(input())

for tc in range(1, T+1):
    # E,N = 간선의 갯수
    E, N=map(int,input().split())
    # 노드 번호는 1~E+1까지 존재하기에 인덱스 0을 비우고 E+1까지 표시하기위해 E+2까지
    a1=[0] * (E+2)
    a2=[0] * (E+2)
    lst=list(map(int,input().split()))
    # 숫자 2개가 하나의 노선을 나타내기에
    for i in range(0,len(lst),2):
        # 첫번째 간선 부모 p 자식 c
        p=lst[i]
        c=lst[i+1]
        # 그걸 a1, a2에 하나씩 넣어줌
        if a1[p]==0:
            a1[p]=c
        else:
            a2[p]=c

    count=0
    inorder(N)
    print(f'#{tc} {count}')