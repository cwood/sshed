from setuptools import setup
from sshed import version

readme_file = open('README.markdown')
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
    packages=['sshed'],
    description='Minimal Parmaiko/ssh2 wrapper to make working with SSH easy.',
)
