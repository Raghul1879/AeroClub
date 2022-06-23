import socket
import threading

PORT = 5050
SERVER = 'localhost'
DISCONNECT = "disconnect"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((SERVER, PORT))

def handle_client(c, addr):
    print(f"{addr} connected")
    while True:
        name=c.recv(1024).decode()
        if name:
            if name == DISCONNECT:
                break
            else:
               print(f"Client: {name}")
               length=len(name)
               c.send(f"Hello {name}! Your name has {length} letters".encode("utf-8"))
            
    c.close()

print("Server is starting...")
s.listen()
while True:
    c, addr = s.accept()
    thread = threading.Thread(target=handle_client, args=(c, addr))
    thread.start()
    print(f"No. of Active connections: {threading.activeCount()-1}")



