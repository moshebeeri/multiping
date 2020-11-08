from abc import ABC, abstractmethod

class Transport(ABC):

  def __init__(self):
    super().__init__()

  @abstractmethod
  def connect(self, host, port):
    pass

  @abstractmethod
  def ping(self, address):
    pass
  
  @abstractmethod
  def pong(self):
    pass

