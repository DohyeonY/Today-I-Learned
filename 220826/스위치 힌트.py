[0, 0, 1, 1, 0, 1, 1, 1]
=> [0, 0, 1, 1, 0, 1, 1, 1]
# arr[4]를 기준으로 좌우의 값이 같은 동안
k = 0
while arr[idx-k] >= 0 and arr[idx+k] <= N and [idx-k] == arr[idx+k] :
    #arr[idx-k]의 값을 반전
    arr[idx+k] = (arr[idx-k] + 1) % 2
    arr[idx+k] = arr[idx-k]
    k += 1

for i in range(len(lst)) :
    print((lst[i] + 1)% 2)

for i in range(len(lst)) :
    print(0 if lst[i] else 1)

