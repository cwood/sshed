from distutils.core import setup
from sshed import version

setup(
    name='sshed',
    author='Colin Wood',
    author_email='cwood06@gmail.com',
    install_requires=[
        'paramiko>=1.7.7.2',
    ],
    long_description=open('README.markdown').read(),
    url='http://cwood.github.com/sshed/',
    version=version,
    packages=['sshed'],
    description='Minimal Parmaiko wrapper to make working with SSH easy.',
)
