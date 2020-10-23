import click
from skyhawk.services import trainer


class Context:
    def __init__(self):
        pass


@click.group()
@click.pass_context
def cli(ctx):
    '''Train skyhawk classifier on captured data'''
    ctx.obj = Context()
    

@cli.command()
@click.pass_context
def train(ctx):
    result = trainer.Facetrainer()
    return result
