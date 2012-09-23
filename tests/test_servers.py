import unittest
from sshed import servers

user = 'vagrant'
password = 'vagrant'
host = '2.3.4.5'


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = servers.Server(host, user=user, password=password)

    def test_run(self):
        self.assertTrue(user in self.server.run('whoami').output)

    def test_sudo(self):
        self.assertTrue('root' in self.server.run('sudo whoami').output)

    def test_passphrase(self):
        self.assertEqual(self.server.run(
            'git clone git@github.com:cwood/sshed', echo=True).returncode, 0)
        self.server.run('rm -rf sshed')

    def test_path(self):
        self.server.run('mkdir ~/dotfiles')
        self.server.run('cd ~/dotfiles')
        self.assertEqual(self.server.run('pwd').output,
                         ['/home/' + user + '/dotfiles'])
        self.server.run('rm -r ~/dotfiles')


class TestServerFromConf(unittest.TestCase):

    def setUp(self):
        self.ssh_config = 'tests/sshconfig'

    def test_creation(self):
        server = servers.from_conf('development', config_file=self.ssh_config)
        self.assertTrue(isinstance(server, servers.Server))
