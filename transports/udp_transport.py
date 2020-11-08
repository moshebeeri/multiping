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
        super().connect(host, port)
        self.sock.bind((host, port))
        print('socket conneted', (host, port))


    def ping(self, address):
        super().ping(address)
        msg = Message().start().json()
        self.sock.sendto(str.encode(msg), address)
        print('ping', msg, address)
        msgFromServer = self.sock.recvfrom(1024)
        msg = "Message from Server {}".format(msgFromServer[0])
        server_msg = Message(json.loads(msgFromServer[0]))
        server_msg.end()
        print('ping time: ', server_msg.time())


    def pong(self):
        super().pong()
        while (True):
            bytesAddressPair = self.sock.recvfrom(1024)
            message = bytesAddressPair[0]
            address = bytesAddressPair[1]
            clientMsg = "Message from Client:{}".format(message)
            clientIP  = "Client IP Address:{}".format(address)
            # pong client
            server_msg = Message(json.loads(message))
            server_msg.add_trace('server')
            self.sock.sendto(str.encode(server_msg.json()), address)

