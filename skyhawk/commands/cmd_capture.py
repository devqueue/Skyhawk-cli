import click
from skyhawk.service import capture

class Context:
    def __init__(self):
        self.capture = capture.Capture()

@click.group()
@click.pass_context
def cli(ctx):
    '''Capture Face data from the desired webcam'''
    ctx.obj = Context()



@cli.command()
@click.pass_context
def color(ctx):
    '''Captures colored face images'''
    result = ctx.obj.capture.color()



@cli.command()
@click.pass_context
def bw(ctx):
    '''Captures black and white face images'''
    result = ctx.obj.capture.bw()
