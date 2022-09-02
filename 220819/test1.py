T = 10

for tc in range(1, T + 1):
    t = int(input())
    words = [list(input()) for _ in range(100)]
    count = 0
    for i in range(100):
        for j in range(100):
            word = ''
            for h in range(100 - j):
                word += words[i][j + h]
                if word == word[::-1]:
                    if count < len(word):
                        count = len(word)

        for j in range(99, -1, -1):
            word = ''
            for h in range(99 - j):
                word += words[i][j + h]
                if word == word[::-1]:
                    if count < len(word):
                        count = len(word)

    for i in range(100):
        for j in range(100):
            word = ''
            for h in range(100 - j):
                word += words[j + h][i]
                if word == word[::-1]:
                    if count < len(word):
                        count = len(word)

        for j in range(99, -1, -1):
            word = ''
            for h in range(99 - j):
                word += words[j + h][i]
                if word == word[::-1]:
                    if count < len(word):
                        count = len(word)

    print(f'#{tc} {count}')