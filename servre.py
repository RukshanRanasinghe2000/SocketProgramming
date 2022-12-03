import socket
from http import server

server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5)
while True:
    print("Server wating for Connection")
    client_socket,address = server_socket.accept()
    print("Client connected from",address)
    while True:
        data = client_socket.recv(1024)
        if not data or data.decode('utf-8')=="END":
            break
        print("recived from client :%s"% data.decode("utf-8"))
        try:
            client_socket.send(bytes('Helloo','utf-8'))
        except:
            print("Exited by user")
    client_socket.close()
server_socket.close()
