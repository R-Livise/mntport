import csv
import os

from process.models import Process

class ProcessService:

  def __init__(self):
    self.table_name = 'data/table_process.csv'

  def create_process(self,process):
    with open(self.table_name, mode='a') as f:
      writer = csv.DictWriter(f,fieldnames=Process.schema())
      writer.writerow(process.to_dict())

  def list_processes(self):
    with open(self.table_name, mode='r') as f:
      reader = csv.DictReader(f,fieldnames=Process.schema())

      return list(reader)

  def get_by_pid_processes(self,pid):
    process_list = self.list_processes()
    process = [process for process in process_list if process['pid'] == pid][0]
    return Process(process['port'],process['pid'],process['line'])

  def get_by_port_processes(self,port):
    try:
      process_list = self.list_processes()
    except FileNotFoundError:
      return False
    process = [process for process in process_list if process['port'] == port][0]
    return Process(process['port'],process['pid'],process['line'])

  def update_process(self,uptade_process):
        processs = self.list_processes()
        uptade_processs = []

        for process in processs:
            if process['port'] == uptade_process.port:
                uptade_processs.append(uptade_process.to_dict())
            else:
                uptade_processs.append(process)

        self._save_to_disk(uptade_processs)

  def delete_process(self,delete_process):
    processs = self.list_processs()
    delete_processs = []

    for process in processs:
      if process['pid'] != delete_process['pid']:
        delete_processs.append(process)
        self._save_to_disk(delete_processs)

  def _save_to_disk(self, processs):
    tmp_table_name = self.table_name + '.tmp'
    with open(tmp_table_name, mode='w') as f:
      writer = csv.DictWriter(f,fieldnames=Process.schema())
      writer.writerows(processs)

    os.remove(self.table_name)
    os.rename(tmp_table_name,self.table_name)