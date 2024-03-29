import socket
from .transport import Transport
from datetime import datetime

class TCPTransport(Transport):
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        super().connect(self, host, port)
        self.sock.connect((host, port))

    def ping(self, address):
        super().ping(address)
        self.sock.sendto(datetime.now(), address)

    def pong(self):
        super().pong()
        while(True):
            bytesAddressPair = self.sock.recvfrom(1024)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            clientMsg = "Message from Client:{}".format(message)
            clientIP  = "Client IP Address:{}".format(address)
            print(clientMsg)
            print(clientIP)
            # pong client
            self.sock.sendto(message, address)

