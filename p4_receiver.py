# Problem 4: UDP receiver - prints emergency alerts with sender's address
import socket

RECEIVER_HOST = "127.0.0.1"
RECEIVER_PORT = 5003

# SOCK_DGRAM = UDP (no connection, no accept/listen needed)
receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver_socket.bind((RECEIVER_HOST, RECEIVER_PORT))
print("Receiver listening for alerts...")

# We know the sender sends 3 alerts, so receive 3 times
for i in range(3):
    alert_data, sender_address = receiver_socket.recvfrom(1024)
    alert_text = alert_data.decode()
    print("Alert:", alert_text, "| From:", sender_address)

receiver_socket.close()
