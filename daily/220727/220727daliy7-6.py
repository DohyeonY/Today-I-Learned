# 객체지향 프로그래밍의 이해와 기...

class Doggy :
    dognum = 0
    dogbir = 0
    
    def __init__(self, name, jong) :
        Doggy.dognum += 1
        Doggy.dogbir += 1
        self.name = name
        self.jong = jong

    def __del__(self) :
        Doggy.dognum -= 1
        
    def status() :
        print(Doggy.dognum)
        print(Doggy.dogbir)
        
    def bark(cls) :
        print('왈왈')
        
dodo = Doggy('dodo', 'bigdog')
dodo.bark()

coco = Doggy('coco', 'smalldog')
coco.bark()

Doggy.status()

del coco

Doggy.status()

