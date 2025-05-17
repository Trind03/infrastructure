import argparse
from defaults import MESSAGER

class Argparser:

    def __init__(self):
        self.Parser = argparse.ArgumentParser(MESSAGER.SOFTWARE_NAME,
                                description=MESSAGER.PROGRAM_DESCRIPTION)

        self.Parser.add_argument("-k","--ssh-key",type=str) # path to local sshkey for authorization to remote server
        self.Parser.add_argument("-t","--time-stamp",type=str) # time-stamp for each update of ssh authorized_keys file.
        self.Parser.add_argument("-r","--remote-url",type=str) # remote server url.
        self.Parser.add_argument("-d","--dist",type=str,) # local path to .ssh folder or location of authorized_keys file.