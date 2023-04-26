# 거품 정렬
N = int(input())
arr = list(map(int,input().split()))

for i in range(N-1, 0, -1): # 구간의 맨 끝 인덱스
    for j in range(i): # 인접원소 중 왼쪽원소 인덱스
        if arr[j] > arr[j+1]: # 오름차순, 더 큰수를 오른쪽으로
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(arr)