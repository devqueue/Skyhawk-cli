import click
from skyhawk.services import detector


class Context:
    def __init__(self):
        pass


@click.command()
def cli():
    '''Start running skyhawk for face recognition'''
    result = detector.run()
    return result



