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

#create a class calculator with add,sub,mul,div methods
