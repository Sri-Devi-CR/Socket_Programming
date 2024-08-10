import socket
import threading


#protocol that tells how many bytes to be received:
#fixed length (bytes) header
HEADER = 64 #has the info about the length of the data which would be received
FORMAT = 'utf-8' #decode the msg to this format

DISCONNECT_MESSAGE = '[TCP CONNECTION TERMINATED]'
#basic requirements of socket:
#constant values are in caps
#port on which the server runs
PORT = 5050 # a port that is not used for something else
#ip address of server
SERVER = "192.168.128.54" #Basically '192.168.0.161', as server should run on my local network, for other systems, it is automatically handled
# gethostbyname - get ip address of this computer by name => socket.gethostbyname(SriDevi-HP)
# gethostname - the name of the computer => print(socket.gethostname())
# binding socket to a specifc address
ADDR = (SERVER, PORT)

#limit of handling the no. of servers
LIMIT = 3

#creating socket:
#opens up the device to other connections
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket() - creates a socket. Arguments - categories of socket
#socket.AF_NET - socket category that indicates acceptable ipv4 addresses for a specific connection
#socket.SOCK_STREAM - streaming data using TCP

#Binding socket to address => anything that connects to ADDR will hit server (socket)
server.bind(ADDR)



#setting up socket for listening and let it wait for connections:
#handles individual connection b/w client and server
def handle_client(conn,addr): #connection and address of client
    print(f"\n[NRE CONNECTION] {addr} connected.")
    connected = True
    while connected:
        #Get information from the connected client
        #number of bytes of data to be received is passed to recv()
        #msg is decoded as the msg received is encoded with a byte format
        msg_length = conn.recv(HEADER).decode(FORMAT) #the result is a string
        #initially msg_length is blank or sumthing like that
        if msg_length:
            msg_length = int(msg_length)
            #Now getting the actual message:
            msg = conn.recv(msg_length).decode(FORMAT)
            #telling the server that connection is closed
            if msg==DISCONNECT_MESSAGE:
                connected = False
                print(msg)
            #printing the received data
##            print(f"[{addr}] said {msg}")
            else:
                print(f"Recv from {addr[1]} :: {msg}")
                #sending a message back to client acknowledging about the received message
                msgToSend = input(">>> ")
                conn.send(msgToSend.encode(FORMAT))
##            conn.send("Msg received".encode(FORMAT))
    conn.close()
#handles connections and distributes it to the necessary function
def start(): # starts the socket server to listen to connections and pass it to handle_client which will run new threads
    server.listen(LIMIT) #listens to the connection made
    print(f"[LISTENING] Server is listening from {SERVER}")
    while True: # terminates when connection is closed
        conn,addr = server.accept() # waits for a new connection
        #when new connection is made - it stores the ip and port it came from
        #conn - socket object that allows connecting to the client that got connected

        #once connection is requested, a thread will begin, basically it is passed to handle_client
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start() # starts the thread

        #printing active connections => printing no. of active threads
        #1 is subtracted because start() thread will always be running
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")
        print(f"Starting chat with {addr[1]}")


print("[STARTING] server is starting......")
start()
