import socket

host = "0.0.0.0"
port = 5000

server = socket.socket()
server.bind((host, port))
server.listen(1)

print("Waiting for connection...")

conn, addr = server.accept()
print("Connected by:", addr)

data = conn.recv(1024).decode()
print("Received command:", data)

# SAFE: just display, not execute
if data == "open_calculator":
    print("Command received to open calculator (not executing for safety)")

conn.close()
