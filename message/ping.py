from datetime import datetime

class Message:
  trace = {}
  def __init__(self):
    self.trace['created'] = datetime.now().timestamp()
  
  def start(self):
    self.trace['start'] = datetime.now().timestamp()
  
  def add_trace(self, ip):
    if ip in self.trace:
       self.trace[ip].append(datetime.now().timestamp())
    else:
      self.trace[ip] = [datetime.now().timestamp()]
  
  def end(self):
    self.trace['end'] = datetime.now().timestamp()

  def get_trace(self):
    return self.trace

  def time(self):
    return self.trace['end'] - self.trace['start']

  def json(self):
    json.dumps(self.__dict__)