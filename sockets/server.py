import socket

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
        print("from connected user"+str(addr)+": " + str(data))
        sendData =input(" -> ")
        conn.send(sendData.encode())

    conn.close()

if __name__ == '__main__':
    server()