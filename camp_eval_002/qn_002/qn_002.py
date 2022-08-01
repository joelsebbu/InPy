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

class Patient:
    def __init__(self, id, name, age, gender, blood):
        self.id=id
        self.name=name
        self.age=age
        self.gender=gender
        self.blood=blood

class CMS:
    def __init__(self,name):
        self.name = name
        self.patients={}
        self.patientCount=0
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

    

jubilee = CMS("jubilee")
#jubilee.initiate()
# jubilee.register(2,'juan','M',22,'B+')
# jubilee.listAll()
# jubilee.search(2)

jubilee.delete(1)
jubilee.listAll()

