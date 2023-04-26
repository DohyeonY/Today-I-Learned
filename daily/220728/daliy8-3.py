# OOP의 상속과 오버라이딩 예제 3

class PublicTransport() :
    count = 0
    def __init__(self, name, fare) :
        self.name = name
        self.fare = fare
        self.passenger = 0

    def get_in(self, num) :
        self.passenger += num
        self.count += num

    def get_off(self, num) :
        self.passenger -= num

    def profit(self) :
        return self.fare * self.count

a = PublicTransport('trail', 5000)
b = PublicTransport('bus', 1000)

a.get_in(500)
a.get_off(5)
print(a.passenger)
print(a.profit())

b.get_in(1800)
b.get_off(56)
print(b.passenger)
print(b.profit())