# Problem 3: File server (TCP) - sends invoice.txt when asked "GET_INVOICE"
import socket

HOST = "127.0.0.1"
PORT = 5002

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server waiting for a client...")

client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

# Receive the client's request
request = client_socket.recv(1024).decode()

# if-else: check the request is valid
if request == "GET_INVOICE":
    # Open the file, read it, send its content
    with open("invoice.txt", "r") as invoice_file:
        file_data = invoice_file.read()
    client_socket.send(file_data.encode())
    print("Invoice sent.")
else:
    client_socket.send("INVALID REQUEST".encode())
    print("Invalid request received.")

client_socket.close()
server_socket.close()
