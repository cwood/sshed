from setuptools import setup, find_packages
from sshed import version
import os

readme_file = open(os.path.abspath(
    os.path.join(os.path.dirname(__file__),'README')))

setup(
    name='sshed',
    author='Colin Wood',
    author_email='cwood06@gmail.com',
    install_requires=[
        'ssh>=1.7.14',
    ],
    long_description=readme_file.read(),
    url='http://cwood.github.com/sshed/',
    version=version,
    packages=find_packages(),
    description='Minimal Parmaiko/ssh2 wrapper to make working with SSH easy.',
)
