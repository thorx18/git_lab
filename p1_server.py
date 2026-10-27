# Problem 1: Echo server (TCP) - converts message to UPPER + lower and sends back
import socket

HOST = "127.0.0.1"   # localhost (your own computer)
PORT = 5000

# 1. Create the server socket (AF_INET = IPv4, SOCK_STREAM = TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind it to an address and port, then start listening
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server waiting for a client...")

# 3. Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

# 4. Receive the message from the client
received_message = client_socket.recv(1024).decode()

# 5. Convert to uppercase and lowercase, send both back
upper_message = received_message.upper()
lower_message = received_message.lower()
client_socket.send((upper_message + " | " + lower_message).encode())

# 6. Close both sockets
client_socket.close()
server_socket.close()
