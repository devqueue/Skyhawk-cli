import click
from skyhawk.services import view




@click.command()
def cli():
	'''View the attandance'''
	result = view.View()
	return result

