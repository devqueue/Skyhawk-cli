import click
from skyhawk.services import capture


class Context:
    def __init__(self):
        pass


@click.group()
@click.pass_context
def cli(ctx):
    '''Capture Face data from the desired webcam'''
    ctx.obj = Context()


@cli.command()
@click.pass_context
def color(ctx):
    '''Captures colored face images'''
    result = capture.Capture.color()
    return result


@cli.command()
@click.pass_context
def black(ctx):
    '''Captures black and white face images'''
    result = capture.Capture.black()
    return result

