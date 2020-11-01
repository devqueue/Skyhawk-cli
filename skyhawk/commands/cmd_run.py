import click
from skyhawk.services import detector


@click.command()
def cli():
    '''Start running skyhawk for face recognition'''
    result = detector.run()
    return result



