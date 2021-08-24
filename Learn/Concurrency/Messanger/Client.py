import socket

host = "127.0.0.1"
port = 50001

def send_message(clientname,message,to):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((host,port))
        encoded_str = str.encode(clientname+ message + to)
        s.sendall(encoded_str)
        data = s.recv(1024)

    print('Received',repr(data))


import time
import datetime as dt

#client = "Client" + str(int(time.time()))
import sys
client = sys.argv[1]

to = ""
while to != "exit":
    to = input("Enter who you want to send:-") 
    send_message(client, " sending " , to)