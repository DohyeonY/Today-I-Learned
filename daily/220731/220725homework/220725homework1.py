# 1. 모음은 몇 개나 있을까?

vowels = ["a", "e", "i", "o", "u"]

def count_vowels(chrs):
    cnt = 0
    for vowel in vowels:
        cnt += chrs.count(vowel)
    return cnt
print(count_vowels("apple"))
print(count_vowels("banana"))
