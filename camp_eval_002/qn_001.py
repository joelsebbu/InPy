import re
import random

class Enterprise:
    def __init__(self):
        self.categories ={}
    @property
    @classmethod
    def capacity(cls):
        return cls.__capacity
    @capacity.setter
    @classmethod
    def capacity(cls,value):
        cls.__capacity = value

class Product:
    def __init__(self,productCode,name,price,category,tax,discount,MRP):
        self.name = name
        self.price = price
        self.category = category
        self.productCode = productCode
        self.tax = tax
        self.discount = discount
        self.MRP = MRP

class Categories(Enterprise):
    def __init__(self,name):
        self.name=name
        self.products = {}
        self.total_products = 0

    def _count(self,code):
        keys  =list(self.products.keys())
        count =0
        regex ='^'+code
        for key in keys:
            if len(re.findall(regex,key)):
                count +=1
        return count

    def addProduct(self,name,price,tax,discount,mrp):
        if self.total_products < self.capacity:
            if len(name)>= 3:
                code = self.name[:2].lower() + name[:3].lower()
                rt =self._count(code)
                code += str(rt)
                r =random.randint(100,999)
                code+=str(r)
                self.products[code] =(Product(code,name,price,self.name,tax,discount,mrp))
                return code
            else:
                print("ProductName too short")
        else:
            print("Already at capacity limit")
        

Enterprise.capacity = 10
abc =Enterprise()
abc.categories['health'] =Categories('health')

print(abc.categories['health'].addProduct('prime',40,4,0,44))
print(abc.categories['health'].addProduct('gaterade',50,10,0,55))


