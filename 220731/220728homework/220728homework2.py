class Animal :
    def __init__(self,name) :
        self.name = name

    def walk(self) :
        print(f'{self.name}! 걷는다!')

    def eat(self) :
        print(f'{self.name}! 먹는다!')

class Dog(Animal) :
    def __init__(self,name) :
        self.name = name

    def run(self) :
        print(f'{self.name}! 달린다!')
    
    def bark(self) :
        print(f'{self.name}! 짖는다!')

class Bird(Animal) :
    def __init__(self,name) :
        self.name = name

    def fly(self) :
        print(f'{self.name}! 푸드덕!')


dog = Dog('꼽이')
dog.run()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()