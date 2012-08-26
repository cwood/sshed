import unittest
from sshed import servers
from .local_ssh import user, password, host


class TestServer(unittest.TestCase):

    def setUp(self):
        self.server = servers.Server(host, user=user, password=password)

    def test_run(self):
        self.assertEqual(self.server.run('whoami'), [user])

    def test_sudo(self):
        self.assertEqual(self.server.run('sudo whoami'), ['root'])

    def test_path(self):
        self.server.run('cd ~/dotfiles')
        self.assertEqual(self.server.run('pwd'),
                         ['/home/' + user + '/dotfiles'])
        self.server.run('cd .vim')
        self.assertEqual(self.server.run('pwd'),
                         ['/home/' + user + '/dotfiles/.vim'])


class TestServerFromConf(unittest.TestCase):

    def test_creation(self):
        server = servers.from_conf('development')
        self.assertTrue(isinstance(server, servers.Server))

    def test_extra_attribute(self):
        server = servers.from_conf('development')
        self.assertTrue(hasattr(server, 'forwardagent'))
