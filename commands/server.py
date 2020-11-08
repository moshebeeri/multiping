class Server:
  def __init__(self, transport):
    self.transport = transport

  def pong(self):
    return self.transport.pong()