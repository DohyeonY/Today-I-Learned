N = int(input())

lst = list(map(int, input().split()))
incnt = 1
decnt = 1
maxc = 1
for i in range(N-1) :

    if lst[i] <= lst[i+1] :
        incnt += 1
        if maxc <= incnt :
            maxc = incnt

    else :

        incnt = 1

for i in range(N - 1):
    if lst[i] >= lst[i+1] :
        decnt += 1
        if maxc <= decnt :
            maxc = decnt

    else :

        decnt = 1

print(maxc)


