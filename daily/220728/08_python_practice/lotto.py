# 여기에 필요한 모듈을 추가합니다.
import random
import json

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []
        

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for _ in range(n):
            oneline = random.sample(range(1, 46), 6)
            oneline.sort()
            self.number_lines.append(oneline)
            # self.number_lines.append(sorted(random.sample(range(1, 46), 6)))
        # print(self.number_lines)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        print('=========================')
        print(f'     제 {draw_number} 회 로또')
        print('=========================')
        strDate = self.get_draw_date(draw_number)
        # t = Lotto.get_draw_date(draw_number)
        print(f'추첨일 : {strDate[0]}/{strDate[1]}/{strDate[2]}')
        print('=========================')
        ch = ord('A')
        for idx in range(len(self.number_lines)):
            print(f'{chr(ch+idx)} : {self.number_lines[idx]}')


    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        print('=========================')
        main_numbers, bonus_number = Lotto.get_lotto_numbers(draw_number)
        print(f'당첨 번호 : {main_numbers} + {bonus_number} ')
        print('=========================')
        ch = ord('A')
        for idx in range(len(self.number_lines)):
            same_main_counts, is_bonus = Lotto.get_same_info(main_numbers, bonus_number, self.number_lines[idx])
            ranking = Lotto.get_ranking(same_main_counts, is_bonus)
            
            output1 = f'{chr(ch+idx)}: {same_main_counts}개 '
            # print(is_bonus)
            output2 = '' if not is_bonus else '+ 보너스 '           
            output3 = f'(낙첨)' if ranking==-1 else f'({ranking}등 당첨!)'
            print(output1 + output2 + '일치' + output3)
            

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        file_data = open(f'./data/lotto_{draw_number}.json')
        file_dict = json.load(file_data)
        # print(file_dict.get('drwNoDate'))
        # t = file_dict.get('drwNoDate').split('-')
        year, month, day = file_dict.get('drwNoDate').split('-')
        return year, month, day
        # return '2021', '03', '24'

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        file_data = open(f'./data/lotto_{draw_number}.json')
        file_dict = json.load(file_data)
        
        main_numbers = []
        for idx in range(1, 7):
            main_numbers.append(file_dict.get(f'drwtNo{idx}'))

        bonus_number = file_dict.get('bnusNo')
        return main_numbers, bonus_number
        
    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = len(set(main_numbers) & set(line))
        is_bonus = bonus_number in line
        # print(main_numbers, bonus_number, line, is_bonus)
        # return 6, True
        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
            return 1
        elif same_main_counts == 5 and is_bonus:
            return 2
        elif same_main_counts <= 2:
            return -1
        else:
            return 8-same_main_counts

        pass
        # return ranking
