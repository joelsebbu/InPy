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
        self.__a = value

    @b.setter
    def b(self, value):
        self.__b = value

    @ans.setter
    def ans(self, value):
        self.__ans = value

    @abstractmethod
    def calculate(self,a,b):
        pass


class Add(Calculate):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def calculate(self):
        self.ans= self.a + self.b


cal =Add(10,20)
cal.calculate
print(cal.ans)