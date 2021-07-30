import uuid

class Report:
  def __init__(self, pid, pcpu, pmem, command, rss,port,datetime, uid=None):
    self.pid = pid
    self.pcpu = pcpu
    self.pmem = pmem
    self.command = command
    self.rss = rss
    self.port = port
    self.datetime = datetime
    self.uid = uid or uuid.uuid4()

  def to_dict(self):
    return vars(self)

  @staticmethod
  def schema():
    return ['uid','pid','pcpu','pmem','command','rss','port','datetime']