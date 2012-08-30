sshed
===================

sshed is a minimal paramiko wrapper that makes working with ssh through python
just like working with it in normal SSH. It will use your configuration that
you have already created first then any extra options can be passed in through
the library that is using it. Servers are base objects that can be extended
to do other tasks. Also the API is dead simple.


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

Creating a new server without a ssh config
```python
from sshed.servers import Server
server = Server(username='username', hostname='development.mycompany.com',
        password='supersecretpassword')

server.run( ... )
```


