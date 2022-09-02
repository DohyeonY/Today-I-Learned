# OPP에 대한 개념 이해 예제2
def wordrelay(word_lst):

    for i in range(1, len(word_lst)):
        # print(i)

        if (word_lst[i - 1][-1] != word_lst[i][0]) or word_lst[i] in word_lst[i - 1: i]:

            return f'{i + 1}번째 참가자가 탈락하였습니다.'

words = ["round","dream","magnet","tweet","tweet","trick","kiwi"]
print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.

