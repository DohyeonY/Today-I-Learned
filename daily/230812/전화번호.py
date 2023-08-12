def solution(phone_number):
    answer = ''
    phone_len = len(phone_number)
    answer += '*' * (phone_len - 4) + phone_number[-4:]
    return answer