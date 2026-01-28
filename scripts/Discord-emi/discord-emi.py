import os
import pathlib
import sys
import argparse

try:
    import rich
    import discord
except ImportError:
    print("\033[33m","Rich or discord is missing to run this script 💫", "\033[0m")
    sys.exit(1)

class DiscordArgParser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("-t",
                                  "--token-file",
                                  help="path to file containing discord api token",
                                  required=True,
                                  type=str,
                                  default=None)

        self.parser.add_argument("-s",
                                 "--server-id",
                                 type=str,
                                 default=None)

        self.parser.add_argument("-d",
                                 "--destination-path",
                                 type=str,
                                 default=None)

        self.args = self.parser.parse_args(sys.argv[1:])


def parse_token_file(token_file: str) -> str:
    token = ""
    with open(token_file, "r") as tf:
        token = tf.read().strip()

    return token

def resolve_abspath(path) -> str:
    if path is None:
        return ""

    return str(pathlib.Path(path).resolve().absolute())


def main() -> int:
    discord_argparser = DiscordArgParser()

    print(parse_token_file(discord_argparser.args.token_file))
    return 0

if __name__ == '__main__':
    sys.exit(main())