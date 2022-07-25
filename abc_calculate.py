from abc import ABC, abstractmethod
#create abstract class Calculate
class Calculate(ABC):

    def __init__(self):
        self.__a = None
        self.__b = None
        self.__ans = None

    @property
    def a(self):
        return self.__a

    @property
    def b(self):
        return self.__b

    @property
    def ans(self):
        return self.__ans

    @a.setter
    def a(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__a = value
        else:
            raise ValueError("a must be a number")
    @b.setter
    def b(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__b = value
        else:
            raise ValueError("b must be a number")

    @ans.setter
    def ans(self, value):
        self.__ans = value

    @abstractmethod
    def calculate(self):
        pass

class Add(Calculate):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        self.ans= self.a + self.b

class Sub(Calculate):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        self.ans= self.a - self.b

class Div(Calculate):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        self.ans= self.a / self.b

class Mul(Calculate):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        self.ans= self.a * self.b

cal =Div(10,20)
cal.calculate()
print(cal.ans)