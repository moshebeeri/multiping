import argparse

if __name__ == '__main__':
    # see https://docs.python.org/2/howto/argparse.html
    # and http://stackoverflow.com/questions/20923640/python-argparse-example
    ap = argparse.ArgumentParser()
    ap.add_argument('-t', '--type', type=str, required=True, help='client, proxy or server')
    ap.add_argument('-i', '--interfaces', nargs='+', default='eth', help='list of interfaces, default local loopback interface')
    ap.add_argument('-p', '--protocols', nargs='+',
                    choices=['udp', 'tcp', 'http-rest'],
                    default='udp',
                    help='list of supported protocols, default to UDP')
    ap.add_argument('-r', "--trace", default=False, help="trace span time")
    args = ap.parse_args()

    if args.type is not None:
      print(args.type)

    if args.interfaces is not None:
      print(args.interfaces)

    if args.protocols is not None:
      print(args.protocols)

    