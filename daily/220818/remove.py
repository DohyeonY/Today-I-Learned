import sys
sys.stdin=open("remove.txt", "r")

T = int(input())                            # testcase

for tc in range(1, T+1) :
    word = input()                          # 문자열 리스트로 입력 받기
    wordlst = []
    # print(wordlst)

    for i in word :                         # 문자열을 하나하나 검사

        if len(wordlst) == 0 :              # 문자열 첫 시작에 값을 넣어주기 위해
            wordlst.append(i)
            continue                        # continue를 안쓰면 바로 아래 if문이 발동해서 계속 pop이 되어버림

        if i == wordlst[-1] :               # 만약 이전 리스트 같은 값이 있으면 이전 값을 지워주기 위해 pop
            wordlst.pop()

        else :                              # s의 값과 같은게 없으면 push
            wordlst.append(i)

    print(f'#{tc} {len(wordlst)}')

    # print(wordlst)
