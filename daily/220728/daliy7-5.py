import random
# OOP의 메서드에 대한 이해와 사용 예제 2

class Pair:
    def __init__(self, student):
        self.student = student
        self.student_number = len(student)
    
    def pick(self, n) :
        return random.sample(self.student,n)
        
        

    def match_pair(self):
        pair_student = []

        while self.student_number > 3:
            pair_student.append(self.pick(2))
            self.student_number -= 2

        pair_student.append(self.pick(self.student_number))

        return pair_student


st_lst = Pair(['김','이','박','최','초이','유','조'])

print(st_lst.match_pair())   