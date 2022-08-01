# Q2. Create a Patient management system python console application that manages records of the patients in a hospital. You may use the MSSQL database

# • Implement basic CRUD operations for this scenario using dictionary in python.
# • There are four operations that are performed, namely, add patient record, update patient record, delete patient record and list with search for patient records.
# • The fields are patientId(int), patientName, gender, age, bloodGroup (string) for every patient.
# • Keep directory with patientId as key and rest as value array corresponding to each key.
# • Prompt user for the operation. 1. Add, 2.Update, 3.Delete, 4.List and Search. Make sure to alert user if a non int or blank value for patientId and blank for other fields.
# • All values should be received using user input only.

import functools
import pyodbc

def connectDB(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn= pyodbc.connect('''
                 
                Driver={SQL Server};
                Server=DESKTOP-UDFFDCR\SQLEXPRESS;
                Database=hospital_db;
                Trusted_Connection=yes; 
        ''')
        except Exception as e:
            print(e)
            print('Database Connection error')
            return None
        else:
            cursor = conn.cursor()
            rt = func(cursor, *args)
            conn.commit()
            conn.close()
            return rt
    return innerWrapper


class CMS:
    def __init__(self,name):
        self.name = name
    @connectDB
    def initiate(cursor,self):
        try:
            cursor.execute(f'''
                Create table {self.name}(
                     patientId int primary key
                    ,patientName varchar(25) not null
                    ,gender varchar(1) not null
                    ,age int not null
                    ,blood varchar(2) not null
                );
            ''')
        except Exception as e:
            print(e)
            print("Table Creation Error")

    @connectDB
    def _search(cursor,self,id):
        cursor.execute(f''' 
            select * from {self.name}
            where patientId = {id} ;
        ''')
        records = cursor.fetchall()
        return len(records),records

    def search(self,id):
        rt=self._search(id)
        print("Id\tName\tGender\tage\tblood")
        for row in rt[1]:
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\n')

    @connectDB
    def addRecord(cursor,self,id,name,gender,age,blood):
        try:
            cursor.execute(f"""insert into {self.name} values({id},'{name}','{gender}',{age},'{blood}');""")
        except Exception as e:
            print(e)
            print("Insert Error")

    def register(self,id,name,gender,age,blood):
        rt= self._search(id)
        if rt[0] == 0:
            self.addRecord(id,name,gender,age,blood)
        else:
            print("Already exist")

    @connectDB
    def listAll(cursor,self):
        cursor.execute(f''' 
            select * from {self.name};
        ''')
        print("Id\tName\tGender\tage\tblood")
        for row in cursor.fetchall():
            print(row[0],'\t',row[1],'\t',row[2],'\t',row[3],'\t',row[4],'\n')

    @connectDB
    def delete(cursor,self,id):
        cursor.execute(f''' 
            delete from {self.name}
            where patientId = {id} ;
        ''')

    @connectDB
    def _update(cursor,self,id,kwargs):
        keys = list(kwargs.keys())
        for key in keys:
            if type(kwargs[key]) is str:
                kwargs[key] = "'"+kwargs[key]+"'"
            cursor.execute(f"""
                update {self.name}
                set {key} = {kwargs[key]}
                where patientId ={id};
            """)
    
    def update(self,id,**kwargs):
        self._update(id,kwargs)
       
            

jubilee = CMS("jubilee")
#jubilee.initiate()

# jubilee.register(2,'juan','M',22,'B+')
# jubilee.listAll()
# jubilee.search(2)

# jubilee.delete(1)
# jubilee.listAll()
# jubilee.update(2,age=2)

def validate(n):

    if type(n) == int:
        return n
    elif n == '':
        n=validate(input("Enter Value again:"))
    elif n=="quit()":
        return 
    return n
        

#create a menu to insert search delete list and update patient record
while(1):
    print("1. Add\n2.Update\n3.Delete\n4.List\n5.Search\n6.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        id = int(input("Enter patientId: "))
        name =validate( input("Enter patientName: "))
        gender = validate(input("Enter gender: "))
        age = validate(int(input("Enter age: ")))
        blood =validate(input("Enter blood type:"))
        jubilee.register(id,name,gender,age,blood)
    elif choice ==2:
        print("\n1.name\n2.gender\n3.age\n4.bloodType")
        ch=int(input())
        if ch ==1:
            id = int(input("Enter id"))
            name =input("Name: ")
            jubilee.update(id,paitentName =name)
        elif ch ==2:
            id = int(input("Enter id"))
            gender =input("gender: ")
            jubilee.update(id,gender =gender)
        elif ch ==3:
            id = int(input("Enter id"))
            age =int(input("Name: "))
            jubilee.update(id,age =age)
        elif ch == 4:
            id = int(input("Enter id"))
            bloodtype =input("bloodType: ")
            jubilee.update(id,blood=bloodtype)
        else:
            print("Invalid Choice")
    elif choice ==3:
        id = int(input("Enter id: "))
        jubilee.delete(id)
    elif choice ==4:
        jubilee.listAll()
    elif choice ==5:
        id = int(input("Enter id: "))
        jubilee.search(id)
    elif choice ==6:
        print("Exiting")
        break
    else:
        print("Invalid Choice")