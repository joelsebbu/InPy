from shutil import ExecError
import pyodbc

def init(conn):
    try:
        conn= pyodbc.connect('''
                 
                Driver={SQL Server};
                Server=DESKTOP-UDFFDCR\SQLEXPRESS;
                Database=emp_db;
                Trusted_Connection=yes; 
        ''')
        print("database connected")
    except Exception as e:
        print(type(e).__name__)
        print("Error: Unable to connect to database")
        return False

    return conn

def createPhonebook(conn):
    try:
        cursor =conn.cursor()
        cursor.execute('''
            create table Contacts(
            name varchar(25)
            ,number int ); 
        ''')
        print("table created")
    except Exception as e:
        print(type(e).__name__)
        print("Create table exception")
    

def addRecord(conn,name,phone):
    try:
        cursor = conn.cursor()
        cursor.execute(''' 
            insert into Contacts(name,number) values(?,?);''',(name,phone)
        )
    except Exception as e:
        print(e)
        print("Insert Error")
    

def searchByName(conn,name):
    cursor=conn.cursor()
    cursor.execute(''' 
        select * from Contacts
        where name = ? ;''',(name)
    )
    print("Name\tNumber")
    for row in cursor.fetchall():
        print(row[0],'\t',row[1])
    

def searchByNumber(conn,phone):
    cursor=conn.cursor()
    cursor.execute(''' 
        select * from Contacts
        where number = ? ;''',(phone)
    )
    print("Name\tNumber")
    for row in cursor.fetchall():
        print(row[0],'\t',row[1])
    

def listAll(conn):

    cursor=conn.cursor()
    cursor.execute(''' 
        select * from Contacts;
    ''')
    print("Name\tNumber")
    for row in cursor.fetchall():
        print(row[0],'\t',row[1])

    

def deleteByName(conn,name):
    cursor=conn.cursor()
    cursor.execute(''' 
        delete from Contacts
        where name = ? ;''',(name)
    )
    # result=[{'name':row[0],'number':row[1]} for row in cursor]
    # print(result)
    

def deleteByNumber(conn,phone):
    cursor=conn.cursor()
    cursor.execute(''' 
        delete from Contacts
        where number = ? ;''',(phone)
    )
    # result=[{'name':row[0],'number':row[1]} for row in cursor]
    # print(result)
    
# initialize connection
conn=None
conn=init(conn)

# create PhoneBook
# createPhonebook(conn)

# add Record to Phonebook
# addRecord(conn,'john',12345)
# addRecord(conn,'juan',23456)
# addRecord(conn,'jamie',34567)
# addRecord(conn,'jordan',45678)

# list all contact
# listAll(conn)

# search by name and number
# searchByName(conn,'juan')
# conn =searchByNumber(conn,12345)

# delete contact by name and number
# deleteByName(conn,'john')
# deleteByNumber(conn,45678)
# listAll(conn)

# commit the connection and close
conn.commit()
conn.close()
