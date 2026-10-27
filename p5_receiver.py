# Problem 5: UDP receiver - checks temperature and prints alert or normal
import socket

RECEIVER_HOST = "127.0.0.1"
RECEIVER_PORT = 5004

receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind((RECEIVER_HOST, RECEIVER_PORT))
print("Receiver listening... (press Ctrl+C to stop)")

while True:
    temperature_data, sender_address = receiver_socket.recvfrom(1024)
    temperature = int(temperature_data.decode())   # bytes -> text -> number

    # if-else: evaluate the temperature
    if temperature > 35:
        print(temperature, "C - High Temperature Alert")
    else:
        print(temperature, "C - Normal")
