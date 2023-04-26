import sys
sys.stdin = open("pizza.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())                    # N = 오븐수 M = 피자수
    Cheeze = [0] + list(map(int, input().split()))      # 피자

    Pan = [0] * N                                       # 오븐
    num = 1                                             # 0번피자 ㄴㄴ 1번피자 ㅇㅇ
    while Pan :                                         # Pan에 피자가 있을때
        pizza = Pan.pop(0)                              # pizza에 Pan 데이터 팝
        Cheeze[pizza] //= 2                             # Cheeze의 pizza번째에 2로 나눈 몫
        if Cheeze[pizza] == 0 :                         # 그게 0이면
            if num <= M :                               # 그리고 num이 전체 피자갯수보다 적거나 같으면
                Pan.append(num)                         # Pan에 num을 넣어줌
                num += 1                                # num에 1을 더해줌
        else :                                          # 0이 아니면 Pan에 pizza를 넣어줌
            Pan.append(pizza)

    print(f'#{tc} {pizza}')

    Sdic = {'S01' : '0', 'S02' : '0', 'S03' : '0', 'S04' : '0',
            'S05' : '0', 'S06' : '0','S07' : '0', 'S08' : '0',
            'S09' : '0', 'S10' : '0', 'S11' : '0', 'S12' : '0',
            'S13' : '0'}
    Ddic = {'D01' : '0', 'D02' : '0', 'D03' : '0', 'D04' : '0',
            'D05' : '0', 'D06' : '0', 'D07' : '0', 'D08' : '0',
            'D09' : '0', 'D10' : '0', 'D11' : '0', 'D12' : '0',
            'D13' : '0'}
    Hdic = {'H01' : '0', 'H02' : '0', 'H03' : '0', 'H04' : '0',
            'H05' : '0', 'H06' : '0', 'H07' : '0', 'H08' : '0',
            'H09' : '0', 'H10' : '0', 'H11' : '0', 'H12' : '0',
            'H13' : '0'}
    Cdic = {'C01' : '0', 'C02' : '0', 'C03' : '0', 'C04' : '0',
            'C05' : '0', 'C06' : '0', 'C07' : '0', 'C08' : '0',
            'C09' : '0', 'C10' : '0', 'C11' : '0', 'C12' : '0',
            'C13' : '0'}