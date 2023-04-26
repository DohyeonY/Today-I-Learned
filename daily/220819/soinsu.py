import sys
sys.stdin=open("soinsu.txt", "r")

T = int(input())                        # testcase

for tc in range(1, T+1) :
    N = int(input())                    # 입력받은 숫자 N

    cnta = 0                            # 각 abcde를 넣을 상자
    cntb = 0
    cntc = 0
    cntd = 0
    cnte = 0
    while True :                       # 그냥 마구 돌리기
        if N % 11 == 0 :                # N이 11로 나누어지면
            N = N / 11                  # N을 11로 나누고
            cnte += 1                   # e에 1을 추가하라

        if N % 7 == 0 :                 # 똑같이 2, 3, 5, 7도 해주고
            N = N / 7
            cntd += 1

        if N % 5 == 0 :
            N = N / 5
            cntc += 1

        if N % 3 == 0 :
            N = N / 3
            cntb += 1

        if N % 2 == 0 :
            N = N / 2
            cnta += 1

        if N == 1 :                     # 만약 N이 1이면 소인수 분해가 끝난거니 브래키
            break

    print(f'#{tc} {cnta} {cntb} {cntc} {cntd} {cnte}')

