class Process:
  def __init__(self,port,pid,line):
    self.port = port
    self.pid = pid
    self.line = line
  
  def to_dict(self):
    return vars(self)

  @staticmethod
  def schema():
    return ['port','pid','line']