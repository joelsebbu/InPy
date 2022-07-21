#create a class calculator with add,sub,mul,div methods
class Calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b
        
    def div(self):
        return self.a/self.b

ob1=Calculator(10,20)
print("sum = ",ob1.add())
print("difference = ",ob1.sub())
print("product = ",ob1.mul())
print("quotient = ",ob1.div())

