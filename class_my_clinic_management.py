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

    def display(self,id):
        print(self.patients[id].id)
        print(self.patients[id].name)
        print(self.patients[id].age)
        print(self.patients[id].dob)
        print(self.patients[id].gender)
        print(self.patients[id].blood)

    def admit(self,name,age,dob,gender,blood):
        id=self.patientCount
        self.patients[id]=(Patient(id,name,age,dob,gender,blood))
        id+=1
        self.patientCount=id
        
    def search(self,id):
        self.display(id)
    def delete(self,name):
        for patient in self.patients:
            if patient.name==name:
                self.patients.remove(patient)
                return
        return None
    def update(self,name,age):
        for patient in self.patients:
            if patient.name==name:
                patient.age=age
                return
        return None
    def listAll(self):
        #print(self.patients[0].name,self.patients[0].age)
        for patient in self.patients:
             self.display(patient) 

clinic = Clinic("clinic","address")
clinic.admit("jane",20,"12/12/12","F","A+")
#clinic.search(0)
clinic.listAll()
# clinic.update("jane",22)
# print(clinic.search("jane").age)