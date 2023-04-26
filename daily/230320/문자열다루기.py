# word = input()
# answer = True
# foundWord = False
# num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# for i in word :
#     if i not in num :
#         answer = False

# print(answer)

def solution(s):
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    answer = 'true'
    for i in s :
        if i not in num :
            answer = 'false'
    return answer

s = input()
print(solution(s))