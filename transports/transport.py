from abc import ABC, abstractmethod

class Transport(ABC):

  def __init__(self):
    super().__init__()

  @abstractmethod
  def connect(self, host, port):
    pass

  @abstractmethod
  def send(self, msg):
    pass
  
  @abstractmethod
  def receive(self):
    pass