import sys
sys.stdin=open("단순2진암호코드.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int(input().split()))