import socket
import threading

nickname = input("Enter a nickname:")

port = 9090
host = '192.168.101.100'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'nick':
                pass
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
            
