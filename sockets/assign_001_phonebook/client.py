import functools
import socket

def connect(func):
    @functools.wraps(func)
    def wrapper(*args):
        host = socket.gethostname()
        port = 5000
        client_socket = socket.socket()

        client_socket.connect((host, port))

        func(*args)

        client_socket.close()
    return wrapper

@connect
def send(client_socket,data):
    client_socket.send(data.encode())
    data = client_socket.recv(1024).decode()
    print(data)

def main():
    print("Welcome to the phonebook")
    print("Type 'q' to quit")
    print("Type 'p' to print the phonebook")
    print("Type 'a' to add a new entry")
    print("Type 'd' to delete an entry")
    print("Type 's' to search by name")
    print("Type 'c' to search by number")
    ch = input(" -> ")
    while ch != 'q':
        if ch == 'p':
            print("Phonebook:")
            print("Name\t\tPhone")
            print("------------------------------")
            print("John\t\t12345")
            print("Mary\t\t54321")
            print("------------------------------")
        elif ch == 'a':
            name = input("Name: ")
            phone = input("Phone: ")
            send(ch+" "+name+" "+phone)
        elif ch == 'd':
            phone = input("Phone: ")
            send(ch+" "+phone)
        elif ch == 's':
            name = input("Name: ")
            send(ch+" "+name)
        elif ch == 'c':
            phone = input("Phone: ")
            send(ch+" "+phone)
        else:
            print("Invalid choice")

        print("Welcome to the phonebook")
        print("Type 'q' to quit")
        print("Type 'p' to print the phonebook")
        print("Type 'a' to add a new entry")
        print("Type 'd' to delete an entry")
        print("Type 's' to search for an entry")
        print("Type 'c' to change an entry")
        ch = input(" -> ")


if __name__ == '__main__':
    main()