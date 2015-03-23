from os import path
from .base import Server
import paramiko as ssh


def from_conf(server, config_file=path.expanduser('~/.ssh/config'),
              server_cls=Server):
    """
        from_conf will create a new server instance based of a server_cls.
        By default this will use the base Server instance to create new
        sub servers. If you extend the ``Server`` class you can override
        this methods server_cls to be the new instance of a Server.

        .. code-block:: python

            from sshed import servers
            server = servers.from_conf('development')
            server.run("whoami").output
            >> ["myusername"]
    """
    def get_sshconfig(config_file):
        if path.exists(config_file):
            with open(config_file) as ssh_conf:
                ssh_config.parse(ssh_conf)
                information = ssh_config.lookup(server)
                if 'port' in information.keys():
                    information['port'] = int(information['port'])
            return information
        else:
            return {}

    ssh_config = ssh.SSHConfig()
    server_config = get_sshconfig(config_file)

    if 'hostname' not in server_config:
        server_config['hostname'] = server

    if issubclass(server_cls, Server):
        server = server_cls(**server_config)
    else:
        raise Exception('Instance not a subclass of Server')

    return server
