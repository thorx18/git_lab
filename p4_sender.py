# Problem 4: UDP sender - sends 3 emergency services, one datagram each
import socket

RECEIVER_HOST = "127.0.0.1"
RECEIVER_PORT = 5003

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

emergency_services = [
    "112: National Emergency",
    "100: Police",
    "108: Ambulance",
]

# for loop: send each string as a separate datagram
for service in emergency_services:
    sender_socket.sendto(service.encode(), (RECEIVER_HOST, RECEIVER_PORT))
    print("Sent:", service)

sender_socket.close()
