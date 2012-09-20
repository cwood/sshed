class Command(object):

    """
        sshed server.run returns back a command object. This object should
        have the return code, stderr, stdout and a couple functions.

        Current this allows a script to retry a command.
    """

    def __init__(cmd, command_str, host):
        cmd.command_str = command_str
        cmd.host = host

    def retry(self):
        return self.host.run(self.command_str)
