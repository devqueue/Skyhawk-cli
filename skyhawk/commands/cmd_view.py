import click
from skyhawk.services import attandance




@click.command()
def cli():
	'''View the attandance'''
	result = attandance.view()
	return result

