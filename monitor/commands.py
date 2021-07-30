import click
import time
import os

from monitor.services import MonitorService
from process.services import ProcessService

@click.group()
def monitor():
  """Manages monitor ports"""
  pass

@monitor.command()
@click.argument('port',
                type=str)
@click.pass_context
def add_port(ctx,port):
  """añadir puerto"""
  process_service = MonitorService.create_service()
  try:
    pid = process_service.add_proccess(port)
  except ValueError:
    click.echo('Port ' + port + ' is not up')
  else:
    click.echo('procces update :' + pid)


@monitor.command()
@click.pass_context
def start(ctx):
  """iniciando proccess"""
  monitor_service = MonitorService.create_service()
  process_service = ProcessService()
  monitor_service.create_file()
  while True:
    try:
      precesses = process_service.list_processes()
    except FileNotFoundError:
      print('There are not ports')
      os._exit(os.EX_OK)

    for process in precesses:
      try:
        monitor_service.add_report(process)
      except ValueError:
        click.echo('port '+ process['port'] + ' not start up ' )
      time.sleep(1)

all = monitor