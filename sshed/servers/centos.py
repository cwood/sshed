from .base import Server


class CentOS(Server):

    def httpd_service(server, action):
        command = server.run('sudo /etc/init.d/httpd %s' % (action))
        if command.returncode is 0:
            return True, command
        else:
            return False, command

    def yum(server, method, package):
        command = server.run('sudo yum %s %s' % (method, package))

        if command.returncode is 0:
            return True, None
        else:
            return False, command.output
