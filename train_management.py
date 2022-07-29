import functools
import pyodbc

def connectDB(func):
    @functools.wraps(func)
    def innerWrapper(*args):
        try:
            conn= pyodbc.connect('''
                 
                Driver={SQL Server};
                Server=DESKTOP-UDFFDCR\SQLEXPRESS;
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
    def checkif(cursor,self,trainId,count,rt):
        if count <5:
           #  print('count',count)
            rt =(trainId,'available')
        else:
            print("Enter first else on ",trainId)
            cursor.execute(f"select _index from Trains where trainId = '{trainId}';")
            index=cursor.fetchall()
            nextIndex=index[0][0]+1
            if nextIndex <= 3: #static #next train shift
                cursor.execute(f"select trainId from Trains where _index = '{nextIndex}'")
                
                self.check(cursor.fetchall()[0][0])
            else: # to wait list
                print("Enter else")
                #self.checkWaitlist(ogTrainId)
        return rt
    @connectDB
    def check(cursor,self,trainId):
        ogTrainId=trainId
        cursor.execute(f''' 
            select count(*) from {trainId}
            where waitList =0;'''
        )
        # print('train id',trainId)
        count =cursor.fetchall()
        rt =(trainId,'unavailable')
        print("count 0 0 ",count[0][0])
        rt=self.checkif(trainId,count[0][0],rt)
       
        print(rt)
        return rt

    @connectDB
    def bookAt(cursor,self,trainId,aadhar,name,fromId,toId):
        cursor.execute(f"insert into Bookings values({aadhar},'{name}','{trainId}');")
        cursor.execute(f"select stId from Stations where name = '{fromId}'")
        fromId =cursor.fetchall()[0][0]
        cursor.execute(f"select stId from Stations where name = '{toId}'")
        toId =cursor.fetchall()[0][0]
        cursor.execute(f"insert into {trainId} values({aadhar},{fromId},{toId},0);")

    def book(self,aadhar,name,fromId,toId):
        trainId = fromId+'_'+toId
        rt=self.check(trainId)
        print("rt",rt)
        #print(rt)
        if rt[1] == 'unavailable':
            print("No Seats Available")
        elif rt[1] == 'available':
            # self.bookAt(rt[0],aadhar,name,fromId,toId,)
            print("Booked a seat on "+rt[0]+". Use your aadhar as ticket")
        elif rt[1] == 'waitList':
            print("You are in the wait list for the train: "+rt[0])


south =Booking()
# south.book(5457,'Joe','TVM','ERN')
# south.book(5458,'kate','TVM','ERN')
# south.book(5459,'jill','TVM','ERN')
south.book(5500,'Matt','TVM','ERN')

