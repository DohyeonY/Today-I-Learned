# 최댓값 구하기

N = int(input())
arr = list(map(int,input().split()))

maxv = 0 # 첫 원소를 최대값으로 가정
for i in range(0, N):
    if arr[i] > maxv :
        maxv = arr[i]
        
print(maxv)

# 최대값의 위치, 같은 값이 있을때는 맨 오른쪽

maxidx = 0 # 첫 원소를 최대값으로 가정
for i in range(0, N):
    if arr[i] >= arr[maxidx] :
        maxidx = i
        
print(maxidx)
