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
        parser = argparse.ArgumentParser()
        parser.add_argument("-t",
                            "--token",
                            help="Discord profile Auth Token",
                            required=True,
                            type=str,
                            default=None)

        parser.add_argument("-s",
                            "--server-id",
                            type=str,
                            default=None)

        parser.add_argument("-d",
                            "--destination-path",
                            type=str,
                            default=None)

        parser.parse_args(sys.argv[1:])


def resolve_abspath(path=None) -> str:
    if path is None:
        return path

    return str(pathlib.Path(path).resolve().absolute())


def main() -> int:
    return 0

if __name__ == '__main__':
    sys.exit(main())