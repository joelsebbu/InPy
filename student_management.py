class Student:
  def __init__(self,rollNo,name,phy,math,che,programming):
    self.rollNo=rollNo
    self.name=name
    self.phy=phy
    self.math=math
    self.che=che
    self.programming=programming

class Management_software:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.students = {}
    self.studentCount=1

  def addRecord(self, name,phy,math,che,programming):
    rollNo=self.studentCount
    self.students[rollNo]=Student(rollNo,name,phy,math,che,programming)
    print("Student added successfully, roll no: %d" % rollNo)
    rollNo+=1
    self.studentCount=rollNo
  
  def __display(self,rollNo):
    print("roll no: ",self.students[rollNo].rollNo)
    print("name: ",self.students[rollNo].name)
    print("phy mark: ",self.students[rollNo].phy)
    print("math mark: ",self.students[rollNo].math)
    print("che mark: ",self.students[rollNo].che)
    print("programming mark: ",self.students[rollNo].programming)
    print('\n')

  def listAll(self):
    for rollNo in self.students:
      self.__display(rollNo)
  
  def search(self, rollNo):
    self.__display(rollNo)

  def delete(self, rollNo):
    print("Deleted student")
    self.__display(rollNo)
    self.students.pop(rollNo)
  
  def update(self, rollNo, **kwargs):
    keys=list(kwargs.keys())
    for key in keys:
      setattr(self.students[rollNo],key,kwargs[key])

sms=Management_software('SMS','Sector-12')
# Question 1: Add a record
sms.addRecord('Raj',90,80,70,60)
sms.addRecord('Anne',80,90,80,70)
sms.addRecord('John',70,80,90,60)
sms.addRecord('Mary',60,70,80,90)
# Question 2: delete a record
#sms.delete(3)
# Question 3: update a record
#sms.update(2,phy=90,programming=90)
# Question 4: list all records
#sms.listAll()
# Question 5: search a record
#sms.search(1)