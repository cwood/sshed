sshed
===================

sshed is a minimal paramiko/ssh2 wrapper that makes working with ssh through
python just like working with it in normal SSH. It will use your configuration
that you have already created first then any extra options can be passed in
through the library that is using it. Servers are base objects that can be
extended to do other tasks. Also the API is dead simple.


Documentation / Repo Information:
---------------------------------
* Documentation: http://sshed.readthedocs.org/en/latest/index.html
* Repo: https://github.com/cwood/sshed


Examples
-------------------
Creating a server from your ~/.ssh/config with ssh keys created. This also
uses a host alias.

```python
from sshed import servers
server = servers.from_conf('development')
server.run('whoami').output
>> ['cwood']
server.run('sudo whoami').output
>> ['root']
server.run('cd /var/www').returncode
>> 0
server.run('pwd').output
>> ['/var/www']
```

Creating a server from just a hostname
```python
from sshed import servers
server = servers.from_conf('myserver.com')
server.run('hostname').output
>> ['myserver.com']
```

Uploading/Downloading from/to a server
```python
from sshed import servers
server = servers.from_conf('development')
server.upload('/tmp/mytar.tar', '/var/tmp/mytar.tar')
server.download('/var/logs/httpd/error_log', '/tmp/remote/error_log')
```

Creating a new server without a ssh config
```python
from sshed.servers import Server
server = Server(username='username', hostname='development.mycompany.com',
        password='supersecretpassword')

server.run( ... )
```

Working with argparse. This sshed module also has a helper for working
with argparse. You can import an action so that when a user puts in a
``--server server.mycompany.com`` it will create a new server instance
for that server.

Example:

```python
from sshed.argparse_actions import ServerAction

# some other argparse information
parser.add_argument('-s', '--server', action=ServerAction, dest='server')
```
