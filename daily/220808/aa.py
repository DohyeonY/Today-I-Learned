# 카운트 정렬
from tkinter import N

N = int(input())
arr = list(map(int,input().split()))


tmp = [0] * N
c = [0] * 101  # 0부터 100까지 숫자 갯수, 인덱스가 100까지 있어야함
for i in range(N): # 카운트
    c[arr[i]] += 1
    
for j in range(1, 101) : # 갯수 누적
    c[j] += c[j-1]
    
for i in range(N-1, -1, -1): # 원본을 뒤에서부터 읽으면서 정렬 결과를 tmp에 저장
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]
print(tmp)
    
