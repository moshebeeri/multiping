import socket
import json
from .transport import Transport
from datetime import datetime
from message.ping import Message

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

    def ping(self, address):
        super().ping(address)
        self.sock.sendto(Message().json(), address)

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
            server_msg = Message(json.loads(message))
            server_msg.append('server')
            self.sock.sendto(server_msg.json(), address)

