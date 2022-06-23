import socket
import time

SERVER='localhost' #Enter ipv4 of server
PORT = 9090
c=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input("Enter your name: ")

start=time.time()

c.sendto(name.encode("utf-8"), (SERVER, PORT))
data, addr = c.recvfrom(1024)

print(data.decode("utf-8"))

end=time.time()

print("Response time", end-start)