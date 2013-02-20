from setuptools import setup, find_packages
from sshed import version

setup(
    name='sshed',
    author='Colin Wood',
    author_email='cwood06@gmail.com',
    install_requires=[
        'ssh>=1.7.14',
    ],
    url='http://cwood.github.com/sshed/',
    download_url='http://github.com/cwood/sshed/tarball/master',
    long_description=open('README.rst').read(),
    version=version,
    include_package_data=True,
    packages=find_packages(),
    description='Minimal Parmaiko/ssh2 wrapper to make working with SSH easy.',
    tests_require=[
        'nose',
    ],
    keywords=['ssh', 'automation', 'remote', 'ssh2', 'OpenSSH'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
    ]
)
