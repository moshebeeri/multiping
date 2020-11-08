
class Client:
  def __init__(self, transport):
    self.transport = transport

  def ping(self, address):
    return self.transport.ping(address)

