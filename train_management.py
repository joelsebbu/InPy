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
            value = func(cursor, *args)
            conn.commit()
            conn.close()
            return value
    return innerWrapper

class Booking:
    def __init__(self):
        pass
        # self.aadhar=aadhar
        # self.name=name
        # self.fromId =fromId
        # self.toId=toId
    @connectDB
    def check(cursor,self,trainId):
        cursor.execute(f''' 
            select count(*) from {trainId}
            where waitList =0;'''
        )
        count=cursor.fetchall()
        return count[0][0]

    def book(self,aadhar,name,fromId,toId):
        trainId = fromId+'_'+toId
        print(trainId)
        rt=self.check(trainId)
        


south =Booking()
south.book(5454,'Joel','TVM','ERN')

