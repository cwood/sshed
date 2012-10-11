.. sshed documentation master file, created by
   sphinx-quickstart on Tue Sep 18 11:49:19 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

sshed documentation
=======================================

Welcome to sshed. The simple to use paramiko wrapper. This little library
makes working with ssh through python like it is working with OpenSSH on your
server, laptop, or anything else that supports OpenSSH2.

Running of the base sshed server with ssh keys.

.. code-block:: python

    from sshed import servers
    server = servers.from_conf('development')
    serve.run('git clone git@github.com:cwood/mysite.com.git', echo=True)
    >> Cloning down ...

Using the CentOS server with a custom run method called yum

.. code-block:: python

    from sshed.servers.centos import CentOS
    server = servers.from_conf('development', server_cls=CentOS)
    server.yum('install', 'python')

Creating a base server without the config.

.. code-block:: python

    from sshed.servers import Server

    server = Server('development.mycompany.com',
                    username='cwood',
                    password='supersecretpassword',
                    port=2222,
                    compress=True)

    server.run('whoami', echo=True)
    >> cwood
    server.run('hostname', echo=True)
    >> development.mycompany.com

.. toctree::
   :maxdepth: 2


.. automodule:: sshed.servers.base
    :members:


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
