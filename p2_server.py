# Problem 2: Chat server (TCP) - receives first, then replies, in a loop
import socket

HOST = "127.0.0.1"
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server waiting for a client...")

client_socket, client_address = server_socket.accept()
print("Connected to:", client_address)

while True:
    # Receive client's message and print it
    client_message = client_socket.recv(1024).decode()
    print("Client:", client_message)

    # If client said "bye", stop the loop
    if client_message == "bye":
        break

    # Ask server user for a reply and send it
    server_reply = input("Server: ")
    client_socket.send(server_reply.encode())

    # If server said "bye", stop the loop
    if server_reply == "bye":
        break

client_socket.close()
server_socket.close()
print("Chat ended.")
