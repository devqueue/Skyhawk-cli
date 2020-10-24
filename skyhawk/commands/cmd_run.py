import click
from skyhawk.services import main


class Context:
    def __init__(self):
        pass


@click.command()
def cli():
    '''Start running skyhawk for face recognition'''
    result = main.run()
    return result



