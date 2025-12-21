import socket

# Pick the server, pick the host, connect with server, send message
SERVER = socket.gethostbyname(socket.gethostname())
PORT = 4321
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(f"Connected with server {SERVER}, {PORT}")

def send_msg(client: socket.socket) -> None:
    while True:
        msg = str(input("Enter your message: ")).encode('utf-8')
        client.sendall(msg)

send_msg(client)