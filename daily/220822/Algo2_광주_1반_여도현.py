T = int(input())                                                        # testcase

for tc in range(1, T+1) :
    N = int(input())                                                    # N = 판의 크기
    arr = [list(map(int, input().split())) for _ in range(N)]           # 전체 판 받아오기
    checklst = [list(map(int, input().split())) for _ in range(3)]      # 3x3 체크해야 할 판 받아오기

    # print(arr)
    # print(checklst)
    result = 0
    for row in range(N) :                                               # 전체 배열 돌리기
        for col in range(N) :
            cnt = 0                                                     # 맞으면 카운트해주기

            for checkrow in range(3) :                                  # 3x3 리스트도 확인해야하기 때문에 돌려주기
                for checkcol in range(3):
                    if 0<= row + checkrow < N and 0 <= col + checkcol < N : # 3x3 리스트만큼을 가장 먼저 돌리면서
                        if arr[row+checkrow][col+checkcol] == checklst[checkrow][checkcol] :   # 맞는지 체크를 하고
                            cnt += 1                                        # cnt에 1씩 추가한다
                        else :                                              # 만약 중간에 한번이라도 일치하지 않으면 바로 cnt = 0으로
                            cnt = 0                                         # 최종 목표인 cnt == 9일때 result를 1 추가하는걸 방해한다

            if cnt == 9 :                                                   # 3x3만큼 돌았을고 cnt가 초기화 되기 전단계에 코드를 넣어줘
                result += 1                                                 # 만약 9칸 모두 일치한다면 result에 +1 해준다

    print(f'#{tc} {result}')
