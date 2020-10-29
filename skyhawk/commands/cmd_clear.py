import click
from skyhawk.services import clear


class Context:
    def __init__(self):
        pass


@click.group()
@click.pass_context
def cli(ctx):
    '''Clear App data'''
    ctx.obj = Context()


@cli.command()
@click.pass_context
def attandance(ctx):
    '''Clear attandance data'''
    result = clear.Clear.attandance()
    return result


@cli.command()
@click.option("--user", type=str, help="Delete data for this user.")
@click.pass_context
def data(ctx, user):
    '''Clear captured images of a user'''
    result = clear.Clear.images(user)
    return result
