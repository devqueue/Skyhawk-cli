from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

setup(
    name='skyhawk',
    version='0.1.0',
    packages=find_packages(),
    include_package_dat=True,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'skyhawk = skyhawk.cli:cli',
            'skyhawk = skyhawk.__main__:main'
        ]
    })
