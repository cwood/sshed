class CommandFailure(Exception):
    """ Raise if the command failed to run succesfully """


class Command(object):

    """
        sshed server.run returns back a command object. This object should
        have the return code, stderr, stdout and a couple functions.

        Current this allows a script to retry a command.
    """

    CommandFailure = CommandFailure

    def __init__(cmd, command_str, host):
        cmd.command_str = command_str
        cmd.host = host

    def retry(self):
        self = self.host.run(self.command_str)
