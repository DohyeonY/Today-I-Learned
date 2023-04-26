def solution(numbers, target):
    answer = 0
    sumResult = [0] # +- 해준 값들을 넣어줄 리스트 생성
    for num in numbers :
        tmp = []
        for i in sumResult :    # 값을 더하고 빼준 배열을 모아놓은 리스트를 for문으로 돌려서
            tmp.append(i + num) # num 값에 더해주고
            tmp.append(i - num) # 빼준 값은 빈 리스트에 넣어줌
        sumResult = tmp         # 그리고 해당 값들은 트리의 가로줄이 되어 sumResult에 들어감

    for i in sumResult :        # 모든 과정을 진행하고 sumResult에 있는 값들 중 target이랑 같은걸 찾아서 answer의 갯수를 찾음
        if i == target :
            answer += 1
    return answer