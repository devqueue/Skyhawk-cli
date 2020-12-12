import click
from skyhawk.services import trainer


@click.command()
def cli():
	'''Train skyhawk classifier on captured data'''
	result = trainer.Facerunnner()
	return result

