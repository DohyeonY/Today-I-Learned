from typing_extensions import Self
# OOP의 상속과 오버라이딩 예제2

class Person :
    def __init__(self, name, age) :
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, birth) :
        age = 2022 - birth + 1
        return Person(name, age)

    def check_age(self) :
        if self.age < 19 :
            return print(True)
        else :
            return print(False)

a = Person.details('nana', 2008)
b = Person.details('nunu', 2000)
print(a.name, a.age, type(a))
print(b.name, b.age, type(b))
a.check_age()
b.check_age()
