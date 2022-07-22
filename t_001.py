"""#print("Hello world")
# decorator function example
def decorator_function(function):
    def wrapper_function():
        print("wrapper function executed before")
        function()
    return wrapper_function

    #function to add two numbers
def add(a,b):
    return a+b
# function print hello world
def print_hello():
    print("Hello world")

decorator_function(print_hello)

def decorator(function):
    def wrapper():
        print("greeting")
        function()
        print("good bye")
    return wrapper

#function to print hello world
@decorator
def print_hello():
    print("Hello world")

print_hello()




#create employee class with emp_count variable
# and inside init name salary is there. also emp_count is incremented
class Employee:
    emp_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1
    def displayCount(self):
        print("Total Employee %d" % Employee.emp_count)
    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

joel=Employee("joel",1000)
joel.displayCount()
joel.displayEmployee()

ben=Employee("ben",2000)
ben.displayCount()
ben.displayEmployee()

print(joel.emp_count)
print(Employee.emp_count) #both are same # but this is not recommended



class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sit(self):
        print("%s is now sitting" % self.name)
    def roll_over(self):
        print(self.name+" is now rolling over")

spike = dog("spike",6)
spike.sit()
spike.roll_over()

#create class rocket with attributes name and distance
class Rocket:
    def __init__(self,name,distance):
        self.name=name
        self.distance=distance
    def launch(self): # return name of rocket and distance
        return self.name+" will be traveling to "+self.distance

class MarsRover(Rocket):
    def __init__(self, name, distance,maker):
        super().__init__(name,distance)#calling parent class constructor
        #Rocket.__init__(self,name,distance) can also be used
        self.maker=maker
    def getMaker(self):
        return self.name+" was made by "+self.maker


x=Rocket("falcon","moon")
y=MarsRover("curiosity","mars","spacex")

print(x.launch())
print(y.launch())
print(y.getMaker())                                         

#create class person with attributes name and age 
#where age is private variable
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age=age

jane=Person("jane",20)
print(jane.getAge())
jane.setAge(21)
print(jane.getAge())


#polymorphism
from turtle import shape


class Shape:
    def __init__(self,name):
        self.name=name
    def draw(self):
        print("drawing "+self.name)

class Circle(Shape):
    
    def draw(self):
        print("drawing circle")

class Rectangle(Shape):
    def draw(self):
        print("drawing rectangle")

shape=Shape("shape")
shape.draw()
circle=Circle("circle")
circle.draw()
rectangle=Rectangle("rectangle")
rectangle.draw()



from ctypes.wintypes import HHOOK


class Avenger:
    @classmethod
    def say_class_method(cls):
        print("class method")
        if(cls.__name__ == "Hero"):
            print("class method of Hero")
        elif(cls.__name__ == "Heroine"):
            print("class method of Heroine")
    
    @staticmethod
    def say_static_method():
        print("static method")

class Hero(Avenger):
    def say_method(self): 
        print("method of Hero")
    
class Heroine(Avenger):
    def say_method(self):
        print("method of Heroine")

hero=Hero()
heroine=Heroine()

hero.say_class_method()
heroine.say_class_method()

hero.say_static_method()
heroine.say_static_method()

"""
class House:
    def __init__(self,price):
        self.__price=price
    
    @property #getter name of function same as variable
    def price(self):
        return self.__price

    @price.setter #setter name of function and wrapper same as variable
    def price(self,price):
         self.__price=price

    @price.deleter #deleter name of function same as variable
    def price(self):
        del self.__price

house=House(100000)
house.price=120000
print(house.price)
del house.price


