#create clinic management system
#does following operations: admit, search, delete, update, listAll

class Patient:
        def __init__(self, id, name, age, dob, gender, blood):
            self.id=id
            self.name=name
            self.age=age
            self.dob=dob
            self.gender=gender
            self.blood=blood

class Clinic:

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.patients={}
        self.patientCount=0

    def __display(self,id):
        print(self.patients[id].id)
        print(self.patients[id].name)
        print(self.patients[id].age)
        print(self.patients[id].dob)
        print(self.patients[id].gender)
        print(self.patients[id].blood)

    def register(self,name,age,dob,gender,blood):
        id=self.patientCount
        self.patients[id]=(Patient(id,name,age,dob,gender,blood))
        id+=1
        self.patientCount=id
        
    def search(self,id):
        self.__display(id)

    def delete(self,id):
        self.patients.pop(id)

    def update(self,id,**kwargs):
        keys = list(kwargs.keys())
        for key in keys:
            setattr(self.patients[id], key, kwargs[key])

    def listAll(self):
        for id in self.patients:
             self.__display(id) 
             print("\n")

clinic = Clinic("clinic","address")
clinic.register("jane",20,"12/12/12","F","A+")
clinic.register("john",21,"12/12/12","M","A+")
clinic.register("Anne",22,"12/12/12","F","B+")

# print("deleting patient with id 1")
# clinic.delete(1)
# print("after deleting")
# clinic.listAll()
clinic.update(2,blood="A-",name="jj")
clinic.search(2)
# print(clinic.search("jane").age)