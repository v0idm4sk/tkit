from setuptools import setup, find_packages

setup(
    name='tkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'getpass',
        'sys'
    ]
)