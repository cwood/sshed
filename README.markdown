sshed
===================

sshed is a minimal paramiko wrapper that makes working with ssh through python
just like working with it in normal SSH. It will use your configuration that
you have already created first then any extra options can be passed in through
the library that is using it. Servers are base objects that can be extended
to do other tasks. Also the API is dead simple.


Examples
-------------------

```python
    from sshed import servers
    server = servers.from_conf('development')
    server.run('whoami')
    >> ['cwood']
    server.run('sudo whoami')
    >> ['root']
    server.run('cd /var/www')
    server.run('pwd')
    >> ['/var/www']
```
