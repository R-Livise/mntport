import click
from monitor import commands as monitor_comands

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {}

cli.add_command(monitor_comands.all)