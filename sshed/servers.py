import paramiko
from getpass import getpass, getuser
from os import path


class Server(object):
    """
        Server is a base class to call ssh commands on. It should used
        like this. The server object should be the base of all environment
        variables for a particular server. The beauty of this is that
        this is self contained and can be used with other tools like
        celery or gevent.

        .. code-block:: python

            from sshed.servers import Server
            development = Server('development.mycompany.com',
                                 username='myusername',
                                 password='mypassword')

            development.run('git clone git@github.com:cwood/mysite.com.git')
            development.run('sudo apachectl restart')

    """

    def __init__(self, hostname, user=None, password=None, **kwargs):

        self.hostname = hostname
        self.username = user
        self.password = password

        if not self.username:
            self.username = getuser()

        if kwargs:
            for key, value in kwargs.iteritems():
                setattr(self, key, value)

        self.cwd = '~'

        self.client = self._setup_client()

    def _setup_client(self):

        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        client.load_system_host_keys()

        try:
            client.connect(self.hostname, username=self.username)
        except paramiko.SSHException:
            try:
                client.connect(self.hostname,
                              username=self.username,
                              password=getpass())

            except:
                raise Exception("User password is wrong or can not access")

        return client

    def commands(self, string, echo=False):
        """
            Use triple quoted strings to send in a mass of shell commands.
            This comes in handy if you need to run a small bash script but
            don't want to do server.run(commanda ... b ... c) in mutiple lines.
        """

        if not '\n' in string:
            raise Exception("Either one command or not triple quoated")

        for command in string.splitlines():
            output = self.run(command)
            if echo:
                print output

    def run(self, command, pty=True):
        """
            run should not treat sudo commands any different then normal
            user commands.

            Need to exapnd this for failed sudo passwords and refreshing
            the channel.
        """

        cd = False

        if 'sudo' in command:
            if self.password is None:
                self.password = getpass('sudo: ')

        if command.startswith('cd'):
            cd, seperator, path = command.partition(' ')

            if not path.startswith(('~', '$', '/')):
                self.cwd = self.cwd + '/' + path
            else:
                self.cwd = path

        channel = self.client.get_transport().open_session()

        if pty:
            channel.get_pty()

        if cd:
            channel.exec_command('cd %s' % (self.cwd))
        else:
            channel.exec_command('cd %s &&' % (self.cwd) + command)

        output = []
        while not channel.exit_status_ready():
            if channel.recv_ready():
                received = channel.recv(1024).splitlines()
                output.append(*received)

                has_sudo = [line for line in received if 'sudo' in line]
                if has_sudo:
                    channel.sendall(self.password + '\n')

        return output

    def upload(self, local_file, remote_path):
        sftp = self.client.open_sftp()
        sftp.put(local_file, remote_path)

    def download(self, remote_path, local_file):
        sftp = self.client.open_sftp()
        sftp.get(remote_path, local_file)


def from_conf(server, config_file=path.expanduser('~/.ssh/config')):
    """
        This will create a new server based of a users config file. It should
        set up various things like forward agent, default usernames, and
        default settings for a server.

        .. code-example:: python
            from sshed import servers
            server = servers.from_conf('development')
            server.run("whoami")
            >> ["myusername"]
    """
    ssh_config = paramiko.SSHConfig()

    with open(config_file) as ssh_conf:
        ssh_config.parse(ssh_conf)

        information = dict(ssh_config.lookup(server))

        if not 'hostname' in information:
            information['hostname'] = server

    server = Server(**information)

    return server
