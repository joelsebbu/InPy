import socket
def send(data):
    host = socket.gethostname()
    port = 5000
    client_socket = socket.socket()

    client_socket.connect((host, port))

    # message = input(" -> ")
    while data != 'q':
        client_socket.send(data.encode())
        rtData = client_socket.recv(1024).decode()
        print("Received from server: " + (rtData))
        message = input(" -> ")

    client_socket.close()

def start():
    send("jj")
if __name__ == '__main__':
    start()