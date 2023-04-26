class Point :

    def __init__(self, x, y) :
        self.x = x
        self.y = y 

class Rectangle :

    def __init__(self, p1, p2):
        self.p1 = p1 # 좌측 상단 좌표
        self.p2 = p2 # 우측 하단 좌표

    def get_area(self) :
        w = abs(self.p2.x - self.p1.x)
        h = abs(self.p1.y - self.p2.y)
        return w * h

    def get_perimeter(self):
        w = abs(self.p2.x - self.p1.x) # 너비
        h = abs(self.p1.y - self.p2.y) # 높이
        return (w + h) * 2

    def is_square(self):

        w = abs(self.p2.x - self.p1.x) # 너비
        h = abs(self.p1.y - self.p2.y) # 높이
        return w == h


p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

