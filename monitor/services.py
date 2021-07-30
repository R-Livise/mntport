import subprocess
import re
import os
import datetime

from process.services import ProcessService
from report.services import ReportService
from process.models import Process
from report.models import Report

class MonitorService:

  monitor = None
  process_service = ProcessService()


  def __init__(self,table_name):
    self.table_name = table_name

  @staticmethod
  def create_service():
    if(not MonitorService.monitor):
      table_name = MonitorService.create_file()
      MonitorService.monitor = MonitorService(table_name)

    return MonitorService.monitor

  @staticmethod
  def create_file():
    today = datetime.datetime.today()
    table_name=today.strftime("results/report%Y-%B-%d.log")
    if not os.path.isfile(table_name):
      MonitorService.write_file(table_name,'USER,PID,%CPU,%MEM,COMMAND,RSS,STARTED,PORT,DATE-HOUR\n')

    return table_name

  @staticmethod
  def write_file(table_name,text):
    with open(table_name, mode='a') as f:
      f.write(text)

  def add_report(self,newprocess):

    process = MonitorService.process_service.get_by_pid_processes(newprocess['pid'])
    today = datetime.datetime.today()
    table_name=today.strftime("results/report%Y-%B-%d.csv")
    if process:
      command_line = 'ps axo user,pid,pcpu,pmem,comm,rss,start | grep ' +  process.pid
      try:
        new_line = subprocess.check_output(command_line, shell=True).decode("utf-8")
      except subprocess.CalledProcessError as error:
        self.add_proccess(process.port)
        return

      if(process.line != new_line):
        extraccion = re.split("\s+", new_line)
        pid =extraccion[1]
        pcpu =extraccion[2]
        pmem =extraccion[3]
        command =extraccion[4]
        rss =extraccion[5]
        now=today.strftime("%Y%B%d %H:%M:%S")

        report = Report(pid, pcpu, pmem, command, rss,process.port,now)
        report_service = ReportService(table_name)
        report_service.create_report(report)
        process.line = new_line

      MonitorService.process_service.update_process(process)
      return True
    else:
        return False

  def add_proccess(self,port):
    try:
      result = subprocess.check_output('netstat -nlp |grep ' + str(port), shell=True)
    except BaseException as error:
      raise ValueError
    else:
      pid = re.search(' (\d+)/', str(result)).group(1)
      process = Process(port,pid,'-')
      if(MonitorService.process_service.get_by_port_processes(port)):
        MonitorService.process_service.update_process(process)
      else:
        MonitorService.process_service.create_process(process)

      return pid
