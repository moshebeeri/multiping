class Proxy:
  def __init__(self, transport):
    self.transport = transport

  def ping(self, address):
    raise NotImplementedError

  def pong(self):
    raise NotImplementedError
