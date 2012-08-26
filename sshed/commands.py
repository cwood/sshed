from sshed.servers import Server
from sshed.exceptions import NotAServer


class Command(str):

    def __init__(cmd, command_str, host):
        cmd.command_str = command_str
        if not isinstance(host, Server):
            raise NotAServer('Instance %s is not a instance of Server'
                             % (host))
        cmd.host = host
