# Problem 5: UDP sender - simulates a temperature sensor
import socket
import random
import time

RECEIVER_HOST = "127.0.0.1"
RECEIVER_PORT = 5004

sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while loop: keep sending random temperatures between 20 and 45
while True:
    temperature = random.randint(20, 45)
    sender_socket.sendto(str(temperature).encode(), (RECEIVER_HOST, RECEIVER_PORT))
    print("Sent:", temperature, "C")
    time.sleep(1)   # wait 1 second between readings
