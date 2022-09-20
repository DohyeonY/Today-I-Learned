import sys
sys.stdin=open("이진수2.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    # '1000' = 5000
    # '0001' = 625
    # '0010' = 1250
    # '0100' = 2500
    N = float(input())

    # 나누기고 빼기 위한 값
    subnum = 1
    # 결과저장
    result = ''
    # 최대 12자리까지 출력하기위해 12번 돌림
    for i in range(12) :
        # 돌릴때마다 반으로 나눠줌
        subnum *= 0.5
        # N에서 subnum을 뺀 값이 0보다 크면 문자 '1'을 추가해주고 N 에 subnum을 빼줌
        if N - subnum >= 0 :
            result += '1'
            N -= subnum
            # N이 0이 되면 끝
            if N  == 0 :
                break
        # 0보다 작으면 결과에 무자 '0'을 추가하고 subnum의 값을 줄이기 위해 다시 위로 돌아감
        else :
            result += '0'
    # 만약 12번 다 돌았는데도 결과값이 있으면 overflow를 출력
    if N :
        result = 'overflow'
    print(f'#{tc} {result}')
