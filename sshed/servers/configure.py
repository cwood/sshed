from os import path
from .base import Server
import ssh

def from_conf(server, config_file=path.expanduser('~/.ssh/config'), server_cls=Server):
    """
        from_conf will create a new server instance based of a server_cls.
        By default this will use the base Server instance to create new
        sub servers. If you extend the ``Server`` class you can override
        this methods server_cls to be the new instance of a Server.

        .. code-block:: python

            from sshed import servers
            server = servers.from_conf('development')
            server.run("whoami")
            >> ["myusername"]
    """
    ssh_config = ssh.SSHConfig()

    with open(config_file) as ssh_conf:
        ssh_config.parse(ssh_conf)

        information = dict(ssh_config.lookup(server))

        if not 'hostname' in information:
            information['hostname'] = server

    if issubclass(server_cls, Server):
        server = server_cls(**information)
    else:
        raise Exception('Instance not a subclass of Server')

    return server
