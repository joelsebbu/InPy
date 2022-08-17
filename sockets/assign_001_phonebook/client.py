
import socket
import json

def toJson(data):
    return json.dumps(data)

def toDict(data):
    return json.loads(data)

def send(data): # dict format
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()
    client_socket.connect((host, port))
    client_socket.send(toJson(data).encode())
    rtData = client_socket.recv(1024).decode()
    client_socket.close()
    return toDict(rtData) # dict format

def display(data):
    print(data['0'])

def start():
    print("Welcome to the phonebook")
    print("Type 'q' to quit")
    print("Type 'p' to print the phonebook")
    print("Type 'a' to add a new entry")
    print("Type 'd' to delete an entry")
    print("Type 's' to search by name")
    print("Type 'c' to search by number")
    ch = input(" -> ")
    while ch != 'q':
        data ={}
        if ch == 'p':
            print("Phonebook:")
            print("Name\t\tPhone")
            data["ch"] ="p"
            rt =send(data)
            display(rt)
        elif ch == 'a':
            name = input("Name: ")
            phone = input("Phone: ")
            data["ch"]=ch
            data["name"]=name
            data["phone"]=phone
            rt =send(data)
            display(rt)
        elif ch == 'd':
            name = input("Name: ")
            data["ch"]=ch
            data["name"]=name
            rt=send(data)
            display(rt)
        elif ch == 's':
            name = input("Name: ")
            data["ch"]=ch
            data["name"]=name
            rt=send(data)
            display(rt)
        elif ch == 'c':
            phone = input("Phone: ")
            data["ch"]=ch
            data["phone"]=phone
            rt=send(data)
            display(rt)
        else:
            print("Invalid choice")

        print("Welcome to the phonebook")
        print("Type 'q' to quit")
        print("Type 'p' to print the phonebook")
        print("Type 'a' to add a new entry")
        print("Type 'd' to delete an entry")
        print("Type 's' to search for an entry")
        print("Type 'c' to search by phone")
        ch = input(" -> ")

if __name__ == '__main__':
    start()