from setuptools import setup
setup(
    name='skyhawk-cli',
    version='1.0',
    packages=['skyhawk-cli'],
    entry_points={
        'console_scripts': [
            'skyhawkcli = skyhawkcli.__main__:main'
        ]
    })
