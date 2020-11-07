from datetime import datetime

class Message:
  trace = {}
  def __init__(self)
    self.trace['created'] = datetime.now()
  
  def start(self):
    self.trace['start'] = datetime.now()
  
  def trace(self, ip):
    if ip in self.trace:
       self.trace[ip].append(datetime.now())
    else:
      self.trace[ip] = [datetime.now()]
  
  def end(self):
    self.trace['end'] = datetime.now()

  def get_trace(self):
    return self.trace
