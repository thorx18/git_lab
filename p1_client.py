# Problem 1: Echo client (TCP)
import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000

# 1. Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to the server
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 3. Ask the user for a message and send it
message_to_send = input("Enter message: ")
client_socket.send(message_to_send.encode())

# 4. Receive the modified message and print it
modified_message = client_socket.recv(1024).decode()
print("Server replied:", modified_message)

# 5. Close the socket
client_socket.close()
