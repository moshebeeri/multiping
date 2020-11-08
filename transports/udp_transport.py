import socket
from .transport import Transport
from datetime import datetime

## see https://docs.python.org/3.8/howto/sockets.html
class UDPTransport(Transport):
    def __init__(self, sock=None):
        super().__init__()
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        super().connect(self, host, port)
        self.sock.connect((host, port))

    def send(self, msg):
        super().send(msg)
        totalsent = 0
        while totalsent < msg.len():
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def receive(self):
        super().receive()
        chunks = []
        bytes_recd = 0
        maxlen = 2048
        while bytes_recd < maxlen:
            chunk = self.sock.recv(min(maxlen - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
            break
        return b''.join(chunks)

    def recvfrom(self, bufferSize):
        bytesAddressPair = self.sock.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client:{}".format(message)
        clientIP  = "Client IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        return message

    def ping(self, address):
        self.sock.sendto(datetime.now(), address)

    def pong(self):
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

