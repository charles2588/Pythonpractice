import socket

#multithreaded server code
from threading import *
import threading

host = "127.0.0.1"
port = 50001


class Message:
    def __init__(self,client,message,to):
        self.client = client
        self.message = message
        self.to = to

class Messages:
    def __init__(self):
        self.my_messages = []

    def store_message(self,client,message,to):
        self.my_messages.append(Message(client,message,to))

    def get_client_messages(self,client):
        final_messages = []
        for msg in self.my_messages:
            if msg.to == client:
                final_messages.append(msg.client +" " +msg.message)
        return final_messages


class Messagingsession(Thread):
    def __init__(self,conn,m):
        super(Messagingsession,self).__init__()
        self.conn = conn
        self.m = m

    def run(self):
        data = self.conn.recv(1024)
        #unpack to client, message and to
        unpacked = data.decode().split(" ")
        client = unpacked[0]
        message = unpacked[1]
        to = unpacked[2]
        m.store_message(client,message,to)
        print(data)
        print(client)
        #read and send any message from other senders
        self.conn.sendall(str.encode(repr(m.get_client_messages(client))))

    

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()

    m = Messages()

    #so start the server and listen at a port for any incoming connection
    while True:
        conn,addr = s.accept()
        client = Messagingsession(conn,m).start()

