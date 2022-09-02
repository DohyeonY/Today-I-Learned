salt = 0
salt_water = 0

while True:
    data = input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오 : ")

    if data == "Done":
        break

    percent, amount = data.split()
    # print(percent, amount)

    salt += int(percent[:-1]) * int(amount[:-1]) / 100   # 퍼센트 * 소금물량 / 100
    
    salt_water += int(amount[:-1])

print(f"{round(salt / salt_water * 100, 2)}% {salt_water}g")