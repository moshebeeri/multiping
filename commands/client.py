
class Client:
  def __init__(self, transport):
    self.transport = transport

  def ping(self):
    return self.transport.ping()

