from sshed import servers
import argparse


class ServerAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, servers.from_conf(values))
