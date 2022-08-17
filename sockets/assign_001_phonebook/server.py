import socket
import json


book ={"jane": "12345", "john": "67890", "anne": "12346"}

def toJson(data):
    return json.dumps(data)

def toDict(data):
    return json.loads(data)

def listAll():
    rt={"0":""}
    for name in book:
        rt["0"] +=(name+" "+book[name]+"\n")
    return rt

def addEntry(data): # in dict format
    book[data["name"]] =data["phone"]
    return {"0":"Entry added"}

def deleteEntry(data): # in dict format
    if data["name"] in book:
        del book[data["name"]]
        return {"0":"Entry deleted"}
    else:
        return {"0":"Entry not found"}

def searchByName(data):
    if data["name"] in book:
        return {"0":book[data["name"]]}
    else:
        return {"0":"Entry not found"}

def searchByPhone(data):
    for name in book:
        if book[name] == data["phone"]:
            return {"0":name}
    
    return {"0":"Entry not found"}

def phoneBook(cmd): # in dict format
    print(cmd)
    rt =cmd
    if cmd["ch"] == 'p':
        rt =listAll()
    elif cmd["ch"] == 'a':
        rt =addEntry(cmd)
    elif cmd["ch"] == 'd':
        rt =deleteEntry(cmd)
    elif cmd["ch"] == 's':
        rt =searchByName(cmd)
    elif cmd["ch"] == 'c':
        rt =searchByPhone(cmd)
    else:
        rt ={"0":"Invalid choice"}
    return rt

def server():
    host =socket.gethostname()
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, addr = server_socket.accept()
    print("Connection from: " + str(addr))
    data = conn.recv(1024).decode()
    print(toDict(data))
    sendData =phoneBook(toDict(data))
    print(sendData)
    conn.send(toJson(sendData).encode())


if __name__ == '__main__':
    while True:
        server()
    