import click
from skyhawk.services import view


class Context:
    def __init__(self):
        pass


@click.group()
@click.pass_context
def cli(ctx):
	'''View the App data'''
	ctx.obj = Context()
	

@cli.command()
@click.pass_context
def attandance(ctx):
	'''View the attandance'''
	result = view.Viewer.view()
	return result


@cli.command()
@click.pass_context
def users(ctx):
	'''View registered users'''
	result = view.Viewer.users()
	return result
