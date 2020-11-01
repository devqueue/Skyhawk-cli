import click
from skyhawk.services import configure


class Context:
    def __init__(self):
        pass


@click.command()
@click.pass_context
def cli(ctx):
    '''Initialize and set dirs for user data'''
    ctx.obj = Context()


@cli.command()
@click.option("--dir", type=str, help="Set this directory for face images.")
@click.pass_context
def imagedir(ctx, imgdir):
    '''Assign a directory for saving face images'''
    result = configure.configdata.imgdir()
    return result


@cli.command()
@click.option("--dir", type=str, help="Set this directory for other user data.")
@click.pass_context
def bindir(ctx, bindir):
    '''Assign a directory for saving face images'''
    result = configure.configdata.bindir()
    return result
