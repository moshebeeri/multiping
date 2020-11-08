import argparse
from transports.udp_transport import UDPTransport
from commands.client import Client
from commands.server import Server

if __name__ == '__main__':
    # see https://docs.python.org/2/howto/argparse.html
    # and http://stackoverflow.com/questions/20923640/python-argparse-example
    ap = argparse.ArgumentParser()
    # TODO: add support for proxy
    ap.add_argument('-t', '--type', type=str, required=True, choices=['client', 'server'], help='client or server')
    # TODO: add more protocols as required
    ap.add_argument('-p', '--protocol', nargs='+',
                    choices=['udp'], # , 'tcp', 'http-rest'],
                    default='udp',
                    help='list of supported protocols, default to UDP')
    # TODO: add tracing printing support
    # ap.add_argument('-r', "--trace", default=False, help="trace span time")
    ap.add_argument('-a', '--ip', type=str, required=True, help='communication ip address')
    ap.add_argument('-o', '--port', type=int, required=True, help='communication port')

    args = ap.parse_args()

    if args.type is not None:
      print(args.type)

    if args.interfaces is not None:
      print(args.interfaces)

    if args.protocols is not None:
      print(args.protocols)

    if args.type == 'client':
      print(args.protocols, 'client')
      transport = UDPTransport()
      Client(transport).ping()

    if args.type == 'server':
      print(args.protocols, 'server')
      transport = UDPTransport()
      transport.connect(args.ip, args.port)
      Server(transport).pong()


    