import socket

SERVER='localhost'
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('socket created!')

s.bind((SERVER, PORT))

print('Waiting for connections')

while True:
    data, addr=s.recvfrom(1024)
    name = data.decode("utf-8")
    print(f"Client: {name}")
    length = len(name)
    s.sendto(f"Hello {name}! Your name has {length} letters".encode("utf-8"), addr)
    