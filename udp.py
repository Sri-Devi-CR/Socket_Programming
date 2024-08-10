import socket
socketClient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
locHost = '192.168.128.33'
portNo = 8080
socketObj = (locHost , portNo)



while True:
    client_input = input("->")
    socketClient.sendto(client_input.encode(), socketObj)
    if client_input == 'exit':
        break

