import sys
sys.stdin = open("input.txt", "r")

tc = 10
for tc in range(1, tc+1):
    n = int(input())
    bl = list(map(int, input().split()))
    # print(n, bl)
    cnt = 0 #초록칠한 부분의 합
    for i in range(2, n-2):
        # print(i)
        h = -1

            # h = -1
        for j in range(i-2, i+3):
            
            if i !=j :
                if h < bl[j] :
                    h = bl[j]
                    
        if bl[i] > bl[i-1] and bl[i] > bl[i-2] and bl[i] > bl[i+1] and bl[i] > bl[i+2]:            
            cnt += bl[i] - h
                    
        # cnt += bl[i] - h
                        
    print(f"#{tc} {cnt}")

