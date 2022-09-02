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


class Bus(PublicTransport) :

    def __init__(self, fare, passenger, limit):
        self.fare = fare
        self.passenger = passenger
        self.limit = limit

    def get_in(self, num) :
        
        super().get_in(num)

        if self.passenger > self.limit :
            return print('더이상 탑승할 수 없습니다.')

a = Bus(1000, 50, 100)
a.get_in(50)
a.get_off(5)

print(a.profit())