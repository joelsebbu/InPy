import socket
def client():
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()

    client_socket.connect((host, port))

    message = input(" -> ")
    while message != 'q':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print("Received from server: " + str(data))
        message = input(" -> ")

    client_socket.close()

if __name__ == '__main__':
    client()