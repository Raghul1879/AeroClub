import socket
import time

PORT=5050
SERVER='localhost'   #Enter ipv4 of server

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

name = input("Enter your name: ")

c.connect((SERVER, PORT))

print("Press enter to know the no. of letters in your name")
input()

start=time.time()
c.send(name.encode("utf-8"))

print(c.recv(1024).decode("utf-8"))

c.send("disconnect".encode("utf-8"))

end=time.time()

print("Response time", end-start)
 