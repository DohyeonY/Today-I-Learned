from typing_extensions import Self
# OOP에 대한 개념 이해 예제 3

class Calculator() :
    # num1 = 0
    # num2 = 0

    def __init__(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2

    def add(self) :
        return self.num1 + self.num2

    def substract(self) :
        return self.num1 - self.num2

    def multuply(self) :
        return self.num1 * self.num2

    def divide(self) :
        try :
            return self.num1 / self.num2

        except :
            return '0으로 나눌 수 없습니다.'

a = Calculator(1, 2)
print(a.add())
b = Calculator(2, 1)
print(b.substract())
c = Calculator(3, 4)
print(c.multuply())
d = Calculator(4, 0)
print(d.divide())
