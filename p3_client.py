# Problem 3: File client (TCP) - requests invoice and saves it
import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send the request string
client_socket.send("GET_INVOICE".encode())

# Receive the file data from the server
received_data = client_socket.recv(4096).decode()

# Write it into a new file
with open("downloaded_invoice.txt", "w") as downloaded_file:
    downloaded_file.write(received_data)
print("Saved as downloaded_invoice.txt")

client_socket.close()
