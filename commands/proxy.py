class Proxy:
  def __init__(self, transport):
    self.transport = transport

  def ping(self):
    return 2

  def listen(self):
    pass
