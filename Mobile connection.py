import socket

host = "YOUR_LAPTOP_IP"
port = 5000

def send_command(cmd):
    client = socket.socket()
    client.connect((host, port))
    client.send(cmd.encode())
    client.close()

# 🎮 MENU
print("1. Open Notepad")
print("2. Show Message")

choice = input("Enter choice: ")

if choice == "1":
    send_command("open_notepad")

elif choice == "2":
    send_command("show_message")

else:
    print("Invalid choice")
