def solution(board):
    answer = 0
    len1 = len(board) + 1
    fstLen1 = len(board[0]) + 1
    arr = [[0] * fstLen1 for _ in range(len1)]
    
    for i in range(1, len1) :
        for j in range(1, fstLen1) :
            if board[i - 1][j - 1] : 
                arr[i][j] = min(arr[i - 1][j], arr[i][j - 1], arr[i - 1][j - 1]) + 1
            
            answer = max(answer, arr[i][j])
    
    return answer ** 2