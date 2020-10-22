from setuptools import setup
setup(
    name='skyhawkcli',
    version='1.0',
    packages=['skyhawkcli'],
    entry_points={
        'console_scripts': [
            'skyhawkcli = skyhawkcli.__main__:main'
        ]
    })
