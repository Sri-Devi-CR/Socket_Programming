import socket

HEADER = 64
PORT = 8080
FORMAT = 'utf-8' 
DISCONNECT_MESSAGE = '[TCP CONNECTION TERMINATED]'
SERVER = "192.168.128.33"#"192.168.0.161"
ADDR = (SERVER,PORT)

#setting up socket for the client:
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connect to server
client.connect(ADDR)

def send(msg):
    #encodes str (msg) in a bytes object
    message = msg.encode(FORMAT)
    #first message is the length of the message
    msg_length = len(message)
    #type casting and encoding length message
    send_length = str(msg_length).encode(FORMAT)
    #send length may vary, hence padding is required to make it to 64 bytes long
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print("Recv :: ",client.recv(2048).decode(FORMAT))
    #decoding the acknowlegment
##    print(client.recv(2048).decode(FORMAT))

print("Connected to server")
mes = input("Type the message and hit enter \n>>> ")
disconnect = ['disconnect','bye','BYE','end']
while (mes not in disconnect):#!= 'disconnect'):
    send(mes)
    mes = input(">>> ")
send(DISCONNECT_MESSAGE)
exit()



















