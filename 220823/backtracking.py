# 백트래킹
def par(k, curSum) :
    if curSum > 10 :
        return

    if k == N :
        if curSum == 10 :
            for i in range(N) :
                if result[i] == 1 :
                    print(lst[i], end=' ')
            print()
        # return
    else :
        result[k] = 0
        par(k + 1, curSum)

        result[k] = 1
        par(k + 1, curSum + lst[k])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 10
result = [-1] * N
par(0, 0)


def n_and_m(depth, n, m):
    if depth == m:
        print(' '.join(map(str, answer)))

    for i in range(1, n + 1):

        if not visited[i]:
            visited[i] = True
            answer.append(i)
            n_and_m(depth + 1, n, m)
            visited[i] = False
            answer.pop()


n, m = map(int, input().split())
visited = [False] * (n + 1)
answer = []

n_and_m(0, n, m)