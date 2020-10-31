from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements


classifiers = [
    'Topic :: Security',
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
    'Intended Audience :: End Users/Desktop',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.7'
]

with open('README.md') as rm:
    RM_desc = rm.read()
    RM_desc = str(RM_desc)

with open('ChangeLog') as cl:
    CL_desc = cl.read
    CL_desc = str(CL_desc)


setup(
    name='skyhawk',
    version='0.1.0',
    description='Skyhawk is a CLI tool that can run on any device with a camera to recognize faces. It built with open-cv & python',
    Long_description=RM_desc + '\n\n' + CL_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/smokedpirate/Skyhawk-cli.git',
    author='Haziq Sayyed',
    author_email='haziq.sayyed@gmail.com',
    license='Mozilla Public License 2.0',
    classifiers=classifiers,
    packages=find_packages(),
    include_package_dat=True,
    install_requires=read_requirements(),
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'skyhawk = skyhawk.cli:cli'
        ]
    })
