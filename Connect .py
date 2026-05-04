import socket
import os

host = "0.0.0.0"
port = 5000

server = socket.socket()
server.bind((host, port))
server.listen(1)

print("Server running... Waiting for connection")

while True:
    conn, addr = server.accept()
    print("Connected:", addr)

    data = conn.recv(1024).decode().strip()
    print("Command:", data)

    # ✅ SAFE COMMAND LIST
    if data == "open_notepad":
        os.system("notepad")   # Windows only

    elif data == "show_message":
        print("Hello from mobile!")

    else:
        print("❌ Unknown or blocked command")

    conn.close()
