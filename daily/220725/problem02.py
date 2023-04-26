def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    lst = 0
    for b in scores :
        if b >= 60 :
            lst += 1
        # print(lst)
    return (lst)
# print(maxs([80, 90, 50, 70]))

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
