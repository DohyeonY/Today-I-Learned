import sys
from tkinter import N
sys.stdin=open("최대상금.txt", "r")

T = int(input())

for tc in range(1, T+1) :
    Nlst, swipNum = map(int, input().split())
    
    print(Nlst, swipNum)