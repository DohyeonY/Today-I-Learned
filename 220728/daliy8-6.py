# 객체지향의 특성과 심화 사용 예제 1

class Point :
    def __init__(self, x, y) :
        self.x = x
        self.y = y


class Rectangle :
    def __init__(self, t1, t2) :
        self.t1 = t1
        self.t2 = t2

    def get_area(self) :
        return abs((self.t1.x - self.t2.x) * (self.t1.y - self.t2.y))

    def get_perimeter(self) :
        return abs((self.t1.x - self.t2.x) * 2) + abs((self.t1.y - self.t2.y) * 2)

    def is_square(self) :
        return abs(self.t1.x - self.t2.x) == abs(self.t1.y - self.t2.y)

a = Point(1, 3)
b = Point(3, 1)
r = Rectangle(a, b)
print(r.get_area())
print(r.get_perimeter())
print(r.is_square())

a = Point(6, 3)
b = Point(3, 6)
r = Rectangle(a, b)
print(r.get_area())
print(r.get_perimeter())
print(r.is_square())




































