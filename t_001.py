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
"""
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