#create clinic management system
#does following operations: admit, search, delete, update, listAll


class Patient:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Clinic:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.patients=[]
    def admit(self,patient):
        self.patients.append(patient)
    def search(self,name):
        for patient in self.patients:
            if patient.name==name:
                return patient
        return None
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
        for patient in self.patients:
            print(patient.name,patient.age) 

clinic = Clinic("clinic","address")
clinic.admit(Patient("jane",20))
clinic.admit(Patient("john",21))
clinic.listAll()
clinic.update("jane",22)
print(clinic.search("jane").age)
