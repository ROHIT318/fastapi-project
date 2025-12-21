import socket
import threading

# 1. Pick the port, pick the server, pick the socket and bind the socket to the server.
SERVER = socket.gethostbyname(socket.gethostname())
# print(socket.gethostname())
# print(f"Local IP Address: {SERVER}")
PORT = 4321
sckt_det = (SERVER, PORT)

sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sckt.bind(sckt_det)


# Handle the client
def handle_client(conn, addr):
    while True:
        msg = conn.recv(100).decode('utf-8')
        if msg != "DISCONNECT...":
            print(f"{addr}: {msg}")
        else:
            conn.close()


# Start the local server
def start_server():
    sckt.listen()
    print("Server is up and running....")
    while True:
        conn, addr = sckt.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(f"Connected with {addr}")
        thread.start()


start_server()
handle_client()