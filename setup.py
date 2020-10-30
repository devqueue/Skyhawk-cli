from setuptools import setup, find_packages

def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: Mozilla Public License 2.0',
    'Programming Language :: Python :: 3',
    'Topic:: Security'
]

setup(
    name='skyhawk',
    version='0.1.0',
    description='Skyhawk is a CLI tool that can run on any device with a camera to recognize faces. It built with open-cv & python',
    Long_description=open('README.md').read +'\n\n' + open('CHANGELOG.md').read(),
    url='https://github.com/smokedpirate/Skyhawk-cli.git',
    author='Haziq Sayyed',
    author_email='haziq.sayyed@gmail.com',
    license='Mozilla Public License 2.0',
    classifiers=classifiers,
    packages=find_packages(),
    include_package_dat=True,
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'skyhawk = skyhawk.cli:cli'
        ]
    })
