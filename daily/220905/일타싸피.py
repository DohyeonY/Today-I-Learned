import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'GWANGJU01_YEODOHYEON'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.

    r = 5.73  # 공의 반지름
    hole_distance = 999999999  # 가까운 홀을 찾기 위해 큰 값을 임의로 지정
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    player_one = [3, 1, 5]
    player_two = [2, 4, 5]
    if order == 1:
        for l in player_one:
            if balls[l][0] >= 1:
                targetBall_x = balls[l][0]
                targetBall_y = balls[l][1]
                break
    elif order == 2:
        for l in player_two:
            if balls[l][0] >= 1:
                targetBall_x = balls[l][0]
                targetBall_y = balls[l][1]
                break

    # 타격포인트와 비교

    distance = math.sqrt((targetBall_x - whiteBall_x) ** 2 + (targetBall_y - whiteBall_y) ** 2)
    target_x = targetBall_x
    target_y = targetBall_y

    for i in range(6):
        x = HOLES[i][0]
        y = HOLES[i][1]

        hit_width = abs(x - targetBall_x)
        hit_height = abs(y - targetBall_y)

        hole_radian = math.atan(hit_width / hit_height)

        hit_x = targetBall_x
        hit_y = targetBall_y

        if targetBall_x > x and targetBall_y > y:
            hit_x += (r * math.sin(hole_radian))
            hit_y += (r * math.cos(hole_radian))
        elif targetBall_x > x and targetBall_y < y:
            hit_x += (r * math.sin(hole_radian))
            hit_y -= (r * math.cos(hole_radian))
        elif targetBall_x < x and targetBall_y < y:
            hit_x -= (r * math.sin(hole_radian))
            hit_y -= (r * math.cos(hole_radian))
        elif targetBall_x < x and targetBall_y > y:
            hit_x -= (r * math.sin(hole_radian))
            hit_y += (r * math.cos(hole_radian))

        # 타격포인트와 흰공까지의 거리
        target_distance = math.sqrt((hit_x - whiteBall_x) ** 2 + (hit_y - whiteBall_y) ** 2)
        # 타격포인트가 타격볼보다 가까운 경우에만
        if distance > target_distance:
            # 홀까지 거리를 계산하고
            target_hole = math.sqrt((targetBall_x - HOLES[i][0]) ** 2 + (targetBall_y - HOLES[i][1]) ** 2)
            # 가장 가까운 홀 찾기
            if hole_distance > target_hole:
                hole_distance = target_hole
                target_x = hit_x
                target_y = hit_y

    width = abs(target_x - whiteBall_x)
    height = abs(target_y - whiteBall_y)

    radian = math.atan(width / height)
    angle = 180 / math.pi * radian
    # 타겟구가 1사분면에 위치
    if target_x > whiteBall_x and target_y > whiteBall_y:
        radian = math.atan(width / height)
        angle = 180 / math.pi * radian
    # 타겟구가 4사분면에 위치
    elif target_x > whiteBall_x and target_y < whiteBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 90
    # 타겟구가 3사분면에 위치
    elif target_x < whiteBall_x and target_y < whiteBall_y:
        radian = math.atan(width / height)
        angle = (180 / math.pi * radian) + 180
    # 타겟구가 4사분면에 위치
    elif target_x < whiteBall_x and target_y > whiteBall_y:
        radian = math.atan(height / width)
        angle = (180 / math.pi * radian) + 270

    distance = math.sqrt(width ** 2 + height ** 2)
    power = (distance * 1.2 + hole_distance * 0.8) / 3.75




    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    #
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')