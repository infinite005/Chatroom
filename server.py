import socket
import threading

Port = 9090
Host = '192.168.101.100'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((Host,Port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client.index(client)
            client.remove(client)
            client.close()
            nickname = nickname[index]
            broadcast(f"{nickname} left the chat!".encode('ascii'))
            nicknames.remove(nickname)
            break

def recieve():
    while True:
        client , address = server.accept()
        print(f"connected with {str(address)}!")

        client.send('nick'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('ascii'))
        client.send("Connected to the server!".encode('ascii'))

        thread = threading.Thread(target=handle,args=(client,))
        thread.start()


print("Server is listening...")
recieve()



        

    
        
 
    
    
