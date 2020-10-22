from setuptools import setup
setup(
    name='skyhawk',
    version='1.0',
    packages=['skyhawk'],
    entry_points={
        'console_scripts': [
            'skyhawk = skyhawk.__main__:main'
        ]
    })
