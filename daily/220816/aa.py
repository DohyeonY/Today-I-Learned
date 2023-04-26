import sys
sys.stdin=open("hoimun2.txt", "r")

for tc in range(10):
    N = int(input())
    characters = [list(input()) for _ in range(100)]
    characters2 = [[characters[i][j] for i in range(100)] for j in range(100)]
    cnt = 100
    found = False
    while cnt >= 1:
        for m in range(100-cnt+1):
            for n in range(100-cnt+1):
                if characters[m][n:n+cnt]==characters[m][n:n+cnt][::-1]:
                    found = True
                if characters2[m][n:n+cnt]==characters2[m][n:n+cnt][::-1]:
                    found = True
        if found == True:
            break
        cnt -= 1
    print("#{} {}".format(N, cnt))