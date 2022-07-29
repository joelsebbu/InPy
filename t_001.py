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


# file handling
fp=open("text.txt","r")
#print(fp.read(10))
print(fp.readline())
print(fp.readline())
print(fp.readline())


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def more(self,a,b):
        self.a=a
        self.b=b
person=Person("jane",20)
person.more(10,20)
print(person.a)
print(person.b)




# higher order function map filter reduce
from functools import reduce
from posixpath import split


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def func(a,b,func):
    return func(a,b)

# print(func(10,20,add))
# print(func(10,20,sub))
# print(func(10,20,mul))


# a=list(map(int,input().split())) #map function takes function as argument and returns list
# print(a)
# c,b=map(int,input().split())
# print(c,b)


#custom function to a map function
def square(x):
    return x*x

a=[1 , 2 , 3 , 4 , 5]
b=list(map(square,a))
print(b)


#custom function to map using lambda
c=list(map(lambda x:x*x*x,a))
print(c)

d=list(filter(lambda x:x%2==0,a))
print(d)

#return if number is odd
def is_odd(x):
    if x%2 != 0:
        return x
e=list(filter(is_odd,a))
print(e)

# combo of map and filter
# f= list(filter(lambda x: x%2==0,map(int, input().split())))
# print(f)

g=reduce(lambda x,y:min(x,y),a)
print(g)
h=reduce(lambda x,y:x+y,a)
print(h)



#abstract class

from abc import ABC,abstractmethod

# class Lion:
#     def __init__(self,name):
#         self.name=name
#     def give_meat(self):
#         print("giving meat to "+self.name)
#     def sleep(self):
#         print("sleep")

# class Panda:
#     def __init__(self,name):
#         self.name=name
#     def give_bamboo(self):
#         print("giving bamboo to "+self.name)
#     def sleep(self):
#         print("sleep")

# class Snake:
#     def __init__(self,name):
#         self.name=name
#     def give_prey(self):
#         print("giving prey to "+self.name)
#     def sleep(self):
#         print("sleep")

# simba = Lion("simba")
# po = Panda("po")
# anaconda = Snake("anaconda")

# simba.give_meat()
# po.give_bamboo()
# anaconda.give_prey()

class Animal(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def do(self,action):
        pass

    @property
    @abstractmethod
    def diet(self):
        pass
    
    @property
    def food(self):
        return self.__food
    
    @food.setter
    def food(self,food):
        if food  in self.diet:
            self.__food=food
        else:
            raise ValueError("invalid food")

class Tiger(Animal):
    def __init__(self,name):
        self.name=name

    @property
    def diet(self):
        return ["meat","grass"]

    def feed(self):
        print(f"giving {self.__food} to "+self.name)

    def do(self,action):
        print(action)

class Lion(Animal):

    @property
    def diet(self):
        return ["meat","fish"]

    def feed(self):
        print(f"giving {self.__food} to "+self.name)

    def do(self,action):
        print(action)

class Panda(Animal):
    def __init__(self,name):
        self.name=name

    @property
    def diet(self):
        return ["bamboo","grass"]

    def feed(self):
        print(f"giving {self._food} to "+self.name)

    def do(self,action):
        print(action)

class Snake(Animal):
    def __init__(self,name):
        self.name=name

    @property
    def diet(self):
        return ["animals","humans"]

    def feed(self):
        print(f"giving {self.__food} to "+self.name)

    def do(self,action):
        print(action)

# simba = Lion("simba")
# po = Panda("po")
# anaconda = Snake("anaconda")
# shereKhan = Tiger("shereKhan")

# shereKhan.feed()
# simba.feed()
# po.feed()
# anaconda.feed()

# zoo=[Lion('simba'),Tiger('shereKhan'),Panda('po'),Snake('anaconda')]
# for animal in zoo:
#     animal.feed()
#     animal.do("sleep %s"%animal.name) 






# file handling
#fp=open("text.txt","r")
#print(fp.read(10))
# print(fp.readline())
# print(fp.readline())
# print(fp.readline())

# lines=fp.readline()
# print(lines)

#append mode
# fp = open("text.txt", "a")
# fp.write("\nhello")

fp=open("text.txt","r")
print(fp.tell())
fp.readline()
print(fp.tell())
#fp.write("hello")  # clears the existing items in file
fp.close()



import os
#create a new directory
#os.mkdir("mydir")
#print current wirking directory
#print(os.getcwd())
#change current working directory
#os.chdir("mydir")
#print(os.getcwd())

#to go back the directory
#os.chdir("..")
#print(os.getcwd())

#delete directory that we created
#os.rmdir("mydir")

result =os.listdir(os.getcwd())
print(result)





import subprocess
with open("text.txt","w") as fp:
    #subprocess.check_call(["python","fileoutputsave.py",stdout=fp])
    subprocess.check_call(["python","fileoutputsave.py"],stdout=fp)



class A:
    def __init__(self,a):
        self.a=a
class B(A):
    def __init__(self):
        super().__init__(self)
    def setVal(self,aa):
        aa.a+=1
        print(aa.a)

aa= A(8)
bb =B()
bb.setVal(aa)
 



 #connect py and mssql
# Set-ExecutionPolicy -Scope CurrentUser 
# Unrestricted 
# -ExecutionPolicy Unrestricted
import pyodbc
conn = pyodbc.connect('''
    Driver={SQL Server};
    Server=DESKTOP-UDFFDCR\SQLEXPRESS;
    Database=emp_db;
    Trusted_Connection=yes;
''')
try:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE EmployeeMaster3(
        Id INT IDENTITY PRIMARY KEY,
        EmployeeCode VARCHAR (10),
        EmployeeName VARCHAR (25),
        DepartmentCode VARCHAR (10),
        LocationCode VARCHAR (10),
        Salary INT
    );
    ''')
except Exception as e:
    print(type(e).__name__)
# for row in cursor:
#     print(row)

print("Checkpoint 1")
try:
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM EmployeeMaster;
    ''')
    # for row in cursor.fetchall():
    #    print(row[2])
    # emp=[{'EmployeeCode':row[1],'EmployeeName':row[2]} for row in cursor.fetchall()]
    # print(emp)

    cursor.execute('''
        Insert into EmployeeMaster3(EmployeeCode,EmployeeName,DepartmentCode,LocationCode,Salary)
        values(?,?,?,?,?);'''
        ,('E002','Johnny','D002','L002',20000))
    cursor.execute('''
        Select * from EmployeeMaster3;
    ''')
    for row in cursor.fetchall():
        print(row)
except:
    print("error in selecting")

conn.commit()
conn.close()




#exception handling
# try:
#     div = 10/10
#     print(div)
# except ZeroDivisionError:
#     print("zero division error")
# except Exception as e:
#     print(e)
#     print(type(e).__name__)
# else:
#     print("no exception")
# finally:
#     print("run no matter what")

#nested try catch
# try:
#     fp=open('tt.txt','a')
#     try:
#         fp.write("hello")
#     except:
#         print("error in writing")
#     finally:
#         fp.close() # have to close the fp pointer no matter what
# except:
#     print('file cannot be opened')

# x='hi'
# if type(x) is not int:
#     raise TypeError("type error")
    
# print("Checkpoint -1")



# create user def exception class
class myError(Exception):
    
    def __init__(self,val):
        self.val =val
    
    def __str__(self):
        return repr(self.val)

class manyError(Exception):
    pass
class divideByZero(manyError):
    pass
try:
    x=0
    if x == 0:
        raise(divideByZero)
    if x is not int:
        raise(myError("Not a number"))
except myError as error:
    print(error)
except divideByZero:
    print("divide by zero")






from re import A


class Car:
    def __repr__(self) :
        return Car.__name__
    pass
car = Car()

class Add:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def __add__(self, other):
        # return self.a+other.a , self.b+other.b # will be a tuple output
        return Add(self.a+other.a , self.b+other.b) # will be an output of the form Add class
    
    def __repr__(self):
        return f'{self.a},{self.b}'

a=Add(3,5)
b=Add(6,8)

c=a+b
print(c)






#dunder class methods


# from re import S


# class Softwares:
#     name=[]
#     versions={}

#     def __init__(self,names) -> None:
#         if names:
#             self.names =names.copy()
#             for name in names:
#                 self.versions[name] =1
#         else:
#             raise Exception("Names cannot be empty")

# # override the str dunder 
# def __str__(self):
#     s=''
#     for key,value in self.versions.items():
#        s+=f'{key}:{value}\n'
#     return s 

# sw1= Softwares(['ps','msword','mspaint'])
# print(sw1)

#demonstrating the class dunder methods
#creating a class with empty list of software  names and an empty dict of software name and version as key value pair
class Softwares:
    name = []
    versions = {} #hold the key value pair of sw and sw version

    #defining (overrriding) the constructor
    #invoked when we create an object and give the names list
    # sw1 = Softwares(['ps','msword','mspaint'])
    def __init__(self,names): #getting sw names as a list
        if names:  # if names is not empty
            self.names = names.copy() #create a copy of the list
            for name in names:
                self.versions[name] = 1 #initialie sw version to 1 for all software names
        else:
            raise Exception("Names cant be empty")
    
    #overriding the str dunder for displaying the list of sws
    #will be invoked when calling print(objname)
    #sw1 = Softwares(['ps','msword','mspaint'])
    #print(sw1)
    def __str__(self):
        #loop through the dictionary and print the list
        s="The list of softwares and its versions are: \n"
        for key,value in self.versions.items():
            s += f"{key} : {value} \n"
        return s

    #overriding the __setitem__ dunder method
    def __setitem__(self,name,version):
        if name in self.versions:
            self.versions[name]=version
        else:
            raise Exception("Name dosent exist")

    def __getitem__(self,name):
        if name in self.versions:
            return self.versions[name]
        else:
            raise Exception('Name dosent exist')

    def __delitem__(self, name):
        if name in self.versions:
            del self.versions[name]
            self.names.remove(name)
        else:
            raise Exception('Name dosent exist')

    def __len__(self):
        return len(self.names)

    def __contains__(self,name):
        rt =False
        if name in self.names:
           rt=True
        return rt 

#creating the software class object
sw1 = Softwares(['ps','msword','mspaint'])
#print the software class object

print(sw1)

# set new version
sw1['msword']=2
print(sw1['msword'])

del sw1['msword']

print(len(sw1))

if 'ps' in sw1:
    print("exist")
else:
    print("Nope")

create and read from csv file
import csv
# with open('sw.csv','r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#Working with csv files using python 
#using the csv module reader() method
import csv  #imiporting the csv module/library

#opening the csv file
file = open("sw.csv")
#using the csv.reader to read the file obj
csvreader = csv.reader(file)

#declaring empty header and rows list
header = []
rows =[]

#using the next()method to read the cirrent line and stop at the start of next line
header = next(csvreader)
print(header)

#using a for loop read the rows below header
for row in csvreader:
    rows.append(row)
print(rows)

#close the file handler
file.close()

#opening csv file without importing any modules
with open('sw.csv') as file:
    content = file.readlines()

#using stip to strip the unwanted char
#using the list comprehension
content = [i.strip() for i in content]
#header will be the first index value
header = content[:1]
#rows will be from first index
rows = content[1:]
print(header)
print(rows)

import csv
#performing write to the csv file
header = ['Names','Experience','Salary']
data = [['Anu',9,40000],['Vinu',8,30000],['Manu',5,25000]]

with open('sw.csv','w',newline="") as file:
    csvwriter = csv.writer(file) #creting the csv writer object
    csvwriter.writerow(header) #write the header contents
    csvwriter.writerows(data) #write the row contents

"""

a=(1,5)
print(a)
a=(2,3)
print(a)