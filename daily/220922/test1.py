from itertools import permutations

'''
시작은 무조건 1부터 끝도 무조건 1로 끝나야 한다 그러면 그 사이에 있어야 할 경로의 경우의 수는
1을 제외하고 순서가 상관 없어서 (총 라인 수 -1)! 이다.
그래서 1에서 시작해서 경우의 수를 거쳐서 결과값을 내놓는 걸 모든 경우의 수 마다 진행해 주고
가장 낮은 값을 value에 넣어 준다.
무조건 1부터 시작하지만 첫 시작을 1부터 하는 이유는 시작 1의 값도 더해야 하기 때문이고 
반대로 도착 지점은 1라인으로 돌아와야 하기 때문에 무조건 마지막 남은 라인의 인덱스 0번째이다.  
'''
T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    permu = [i for i in range(2, N+1)]
    value = 9999999999
    # print(room_list)
    for j in permutations(permu, N-1) :
        # print(j)
        s = 1
        result = 0
        for k in j :
            # print(k)
            result += arr[s - 1][k - 1]
            s = k
        result += arr[s - 1][0]
        if value > result :
            value = result
    print(f'#{tc} {value}')