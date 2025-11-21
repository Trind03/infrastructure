from argparse import ArgumentParser

class BinArgumentParser:
    def __init__(self):
        self.parser = ArgumentParser(
            description='Binary convirter',
        )
        self.parser.add_argument(
            "--file",
            type=str,
            help="Name of target file.",
            default=None
        )
        self.parser.add_argument(
            "--binary-flags",
            type=str,
            help="Flags for processing to binary data.",
            default=None
        )