# 객체지향의 특성과 심화 사용 예제 2

from typing_extensions import Self


class Stack :
    def __init__(self) :
        self.lst = []

    def empty(self) :
        if self.lst == [] :
            return True
        else :
            return False

    def top(self) :
        a = self.lst[-1]
        if self.lst == [] :
            return None
        else :
            return a

    def pop(self) :
        b = self.lst[-1]
        del self.lst[-1]
        if self.lst == [] :
            return None
        else :
            return b

    def push(self, d) :
        self.lst.append(d)

    def __repr__(self) :
        return repr(self.lst)

a = Stack()
a.push('a')
a.push('b')

print(a.top())
print(a.pop())

a.push('c')

print(a.top())
print(a.__repr__())

