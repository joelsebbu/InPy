#create clinic management system
#does following operations: admit, search, delete, update, listAll

from asyncio.windows_events import NULL


class Patient:
        def __init__(self, id, name, age, dob, gender, blood):
            self.id=id
            self.name=name
            self.age=age
            self.dob=dob
            self.gender=gender
            self.blood=blood
            self.admitted =False
            self.token=NULL
            self.docID =NULL

class Clinic:

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.patients={}
        self.patientCount=0

    def __display(self,id):
        print("ID: ",self.patients[id].id)
        print("Name: ",self.patients[id].name)
        print("Age: ",self.patients[id].age)
        print("DOB: ",self.patients[id].dob)
        print("Gender: ",self.patients[id].gender)
        print("Blood: ",self.patients[id].blood)
        print("Admitted: ",self.patients[id].admitted)
        print("Admitted to doctor: ",self.patients[id].docID)
        print("current holding token ID: ",self.patients[id].token)

    def register(self,name,age,dob,gender,blood):
        id=self.patientCount
        self.patients[id]=(Patient(id,name,age,dob,gender,blood))
        rtid =id
        id+=1
        self.patientCount=id
        return rtid

    def search(self,id):
        self.__display(id)

    def delete(self,id):
        print("Deleted patient with id: ",id)
        self.__display(id)
        self.patients.pop(id)

    def update(self,id,**kwargs):
        keys = list(kwargs.keys())
        for key in keys:
            setattr(self.patients[id], key, kwargs[key])

    def listAll(self):
        for id in self.patients:
             self.__display(id) 
             print("\n")

class IP(Clinic):
    def __init__(self,clinic,name,address):
        super().__init__(name,address)
        self.tokenCount=1
        self.clinic=clinic
    def admit(self,id,docname):
        print("Admitted patient with id: ",id)
        #super.__display(id)
        self.clinic.patients[id].admitted=True
        self.clinic.patients[id].token=self.tokenCount
        self.clinic.patients[id].docname=docname
        self.tokenCount+=1
        #self.search(id)
        return "tokenID",self.clinic.patients[id].token
    
    def discharge(self,id):
        print("Discharged patient with id: ",id)
        #super.__display(id)
        self.clinic.patients[id].admitted=False
        self.clinic.patients[id].token=NULL
        self.clinic.patients[id].docID=NULL
        self.clinic.docname=NULL
        #self.search(id)
        return "tokenID",self.clinic.patients[id].id

class OP(Clinic):
    def __init__(self,name,address):
        super().__init__(name,address)
        self.tokenCount=1
    def admit(self,name,age,dob,gender,blood,docname):
        id =super().register(self,name,age,dob,gender,blood)
        print("Admitted patient with id: ",id)
        self.__display(id)
        self.patients[id].admitted=True
        self.patients[id].token=self.tokenCount
        self.docname=docname
        self.tokenCount+=1
        return "tokenID",self.patients[id].token
    
    def discharge(self,id):
        print("Discharged patient with id: ",id)
        self.__display(id)
        self.patients[id].admitted=False
        self.patients[id].token=NULL
        self.patients[id].docID=NULL
        self.docname=NULL
        return "tokenID",self.patients[id].id

clinic = Clinic("clinic","address")
clinic.register("jane",20,"12/12/12","F","A+")
clinic.register("john",21,"12/12/12","M","A+")
clinic.register("Anne",22,"12/12/12","F","B+")

#print("deleting patient with id 1")
#clinic.delete(1)
#print("after deleting")

#print("lsiting all patients")
#clinic.listAll()

#print("Update patient with id 2")
#clinic.update(2,blood="A-",name="jj")

#print("Searching for patient with id 2")
#clinic.search(2)

# op = OP("op-1","kims")
ip = IP(clinic,"ip-1","kims")

print(ip.admit(2,"doc1"))

# clinic.admit(2)
