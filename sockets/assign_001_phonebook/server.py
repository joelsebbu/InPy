import socket

def phoneBook(data):
    cmd =list(data.split())
    if cmd[0] == 'p':
        pass

def server():
    host =socket.gethostname()
    port = 5000
    server_socket = socket.socket()

    server_socket.bind((host, port))
    server_socket.listen(2)
    conn, addr = server_socket.accept()
    print("Connection from: " + str(addr))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        sendData =phoneBook(data)
        conn.send(sendData.encode())

    conn.close()

if __name__ == '__main__':
    server()