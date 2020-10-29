#!venv/bin/python3.8
import click
from skyhawk.services import attandance




@click.command()
def cli():
	'''View the attandance'''
	result = attandance.view()
	return result

