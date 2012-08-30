class Command(object):

    def __init__(cmd, command_str, host):
        cmd.command_str = command_str
        cmd.host = host

    def retry(self):
        return self.host.run(self.command_str)
