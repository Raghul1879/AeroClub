import socket

SERVER = 'localhost'   
PORT = 9092
msg = "measure temp"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((SERVER, PORT))

print("Server is starting...")
s.listen(0)

while True:
    c, addr = s.accept()
    print("Connected with", addr)
    c.send(bytes(msg,'utf-8'))
    c.close()