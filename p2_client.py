# Problem 2: Chat client (TCP) - sends first, then waits for reply, in a loop
import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5001

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True:
    # Client types a message and sends it
    client_message = input("Client: ")
    client_socket.send(client_message.encode())

    # If client said "bye", stop the loop
    if client_message == "bye":
        break

    # Wait for the server's reply and print it
    server_reply = client_socket.recv(1024).decode()
    print("Server:", server_reply)

    # If server said "bye", stop the loop
    if server_reply == "bye":
        break

client_socket.close()
print("Chat ended.")
