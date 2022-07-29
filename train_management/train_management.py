import functools
import pyodbc

def connectDB(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn= pyodbc.connect('''
                 
                Driver={SQL Server};
                Server=DESKTOP-AFJLVL3\SQLEXPRESS;
                Database=IRCTC;
                Trusted_Connection=yes; 
        ''')
        except:
            print('Database Connection error')
            return None
        else:
            cursor = conn.cursor()
            rt = func(cursor, *args)
            conn.commit()
            conn.close()
            return rt
    return innerWrapper

class Booking:
    def __init__(self):
        pass
        # self.aadhar=aadhar
        # self.name=name
        # self.fromId =fromId
        # self.toId=toId
    @connectDB
    def showPassengers(cursor,self,trainId):
        cursor.execute(f"select * from {trainId} where waitList = 0")
        print("aadhar\tFrom\tTo")
        for i in cursor:
            print(i[0],"\t",i[1],"\t",i[2])

    @connectDB
    def check(cursor,self,trainId,waitList=0,max=5):
        ogTrainId=trainId
        cursor.execute(f''' 
            select count(*) from {trainId}
            where waitList ={waitList};'''
        )
        # print('train id',trainId)
        count =cursor.fetchall()
        rt =(trainId,'unavailable')
        print("count 0 0 ",count[0][0])
        if count[0][0] <max:
           #  print('count',count)
            if waitList == 0: 
                rt =(trainId,'available')
            elif waitList == 1:
                rt=(trainId,'waitList')
        else:
            print("Enter first else on ",trainId)
            cursor.execute(f"select _index from Trains where trainId = '{trainId}';")
            index=cursor.fetchall()
            nextIndex=index[0][0]+1
            if nextIndex <= 3: #static #next train shift
                cursor.execute(f"select trainId from Trains where _index = '{nextIndex}'")
                
                rt = self.check(cursor.fetchall()[0][0])
            else: # to wait list
                rt =self.check(ogTrainId,1,2)
        print(rt)
        return rt

    @connectDB
    def bookAt(cursor,self,trainId,aadhar,name,fromId,toId,waitList=0):
        print("Inside book at")
        cursor.execute(f"insert into Bookings values({aadhar},'{name}','{trainId}');")
        cursor.execute(f"select stId from Stations where name = '{fromId}'")
        fromId =cursor.fetchall()[0][0]
        cursor.execute(f"select stId from Stations where name = '{toId}'")
        toId =cursor.fetchall()[0][0]
        cursor.execute(f"insert into {trainId} values({aadhar},{fromId},{toId},{waitList});")

    def book(self,aadhar,name,fromId,toId):
        trainId = fromId+'_'+toId
        rt=self.check(trainId)
        print("rt",rt)
        #print(rt)
        if rt[1] == 'unavailable':
            print("No Seats Available")
        elif rt[1] == 'available':
            self.bookAt(rt[0],aadhar,name,fromId,toId)
            print("Booked a seat on "+rt[0]+". Use your aadhar as ticket")
        elif rt[1] == 'waitList':
            print("You are in the wait list for the train: "+rt[0])


south =Booking()
#create a menu to book a ticket and show the list of passengers
while 1:
    print("1. Book a ticket")
    print("2. Show the list of passengers")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        aadhar = int(input("Enter your aadhar: "))
        name = input("Enter your name: ")
        fromId = input("Enter your from station: ")
        toId = input("Enter your to station: ")
        south.book(aadhar,name,fromId,toId)
    elif choice == 2:
        trainId = input("Enter the train id: ")
        south.showPassengers(trainId)
    elif choice == 3:
        print("Thank you for using our service")
        exit()
    else:
        print("Invalid choice")
        exit()
