import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수63
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.\

    while True: 
        number = int(input("1이상 10000이하의 숫자를 입력하세요.:"))

        if number<1 or number>10000:
            print("잘못된 범위의 숫자를 입력했습니다. 다시 입력해주세요.")
            continue

        counts = counts+1

        if number>answer:
            print("DOWN!!!!")
        elif number<answer:
            print("UP!!!")
        else:
            print(f"CORRECT!!! {counts}회 만에 정답을 맞추셨습니다")
            print()
            break

    command = input("게임을 재시작 하시려면 y, 종료하시려면 n을 입력하세요:")

    if command =='y':
        print()
        continue

    if command =='n':
        print("이용해주셔서 감사합니다.게임을 종료합니다.")
    else:
        print("잘못된 값을 입력하셨습니다. 게임을 종료합니다.")

    is_playing = False