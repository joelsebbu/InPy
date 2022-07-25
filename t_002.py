#imiporting the abstract class and the decorator ftom the abc module
from abc import ABC, abstractmethod

#declaring the Abstract Base class from ABC
class Animal(ABC):
    @abstractmethod   #decorator for abstract method
    def feed(self,action): 
        pass  #just a placeholder to escape the empty function error

    #define a diet property using the decorator 
    #and abstract method
    @property
    @abstractmethod
    def diet(self): #define diet property
        pass
    
    @property
    def food_eaten(self):  
        #define the food_eaten property
        #food_eaten property's gettter
        return self.__food

    #having the setter for food_eaten
    @food_eaten.setter
    def food_eaten(self,food):
        if food in self.diet:
            self.__food = food    
        else:
            raise ValueError(f"this animal doesn't eat this")
    
    @abstractmethod   #decorator for abstract method
    def do(self,action): #action is an abstract function parameter
        pass  #just a placeholder to escape the empty function error


#class and regular fns inheriting abstract class
class Lion(Animal):
    @property
    def diet(self):
        return ["antelope","cheetah","buffalo"]

    def feed(self):
        print(f"Feeding a lion with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} lion with raw meet at {time}")

class Panda(Animal):
    @property
    def diet(self):
        return ["bamboo","leaves"]

    def feed(self):
        print(f"Feeding a panda with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} panda with bamboo at {time}")

class Snake(Animal):
    @property
    def diet(self):
        return ["mice","rabbit"] 

    def feed(self):
        print(f"Feeding a snake with {self.food_eaten}")

    def do(self,action,time):    
        #must implement feed because its an abstrct method
        #must include action because its an abstrct method parameter
        print(f"{action} snake with mice at {time}")

simba = Lion()
simba.food_eaten="buffalo"
simba.feed()
kungfupanda = Panda()
kingkobra = Snake()