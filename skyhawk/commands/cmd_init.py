import click
from skyhawk.services import initialize


@click.command()
def cli():
    '''Start running skyhawk for face recognition'''
    result = initialize.run()
    return result
