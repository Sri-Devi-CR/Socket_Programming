import socket
socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
locHost = '192.168.128.33'
portNo = 8080


socketClient.connect((locHost,portNo))
print("Connection Established!")

while True:
    client_input = input("->")
    socketClient.send(client_input.encode())
    if client_input == 'exit':
        break
    server_msg = socketClient.recv(2048)
    print("Server:",server_msg.decode())
socketClient.close()