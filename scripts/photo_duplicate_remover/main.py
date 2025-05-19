"""Application for iterating reqursavly thro an library,
of photos and remove or point out duplicates"""

import argparse
import sys
import os
import hashlib
from defaults import ARGUMENT_DESCRIPTOR


class ARGUMENTPARSER:
    """Program spesific wrapper around argparse."""

    def __init__(self):
        self.root_path = None

        self.parser = argparse.ArgumentParser("photorm")

        self.parser.add_argument(
            "-k", "--kill", action="store_true", help=ARGUMENT_DESCRIPTOR.KILL
        )

        self.parser.add_argument(
            "--wsroot", type=str, help=ARGUMENT_DESCRIPTOR.WSROOT, default=getcwd()
        )

        self.parser.add_argument(
            "--infra-mode",
            action="store_true",
            default=False,
            help=ARGUMENT_DESCRIPTOR.INFRA_MODE,
        )

        self.argv = self.parser.parse_args(sys.argv[1:])


def hash_my_stuff(filename, algoithm="sha256", read_block_size=128):
    """Reads file in chunks & returns checksum of contents.

    Args:
        filename (str): filename if file to be read.
        algoithm (str, optional): hashing algorithm to be used. Defaults to "sha256".
        read_block_size (int, optional): chunk size of each read & hash iteration. Defaults to 128.

    Returns:
        str: file checksum of spesified algorithm.
    """
    composite = hashlib.new(algoithm)
    try:
        with open(filename, "rb") as file:
            while chunk := file.read(read_block_size):
                composite.update(chunk)
        return composite.hexdigest()

    except Exception as error:
        print(error)


def find_files(root_path) -> dict[str]:
    """Find all duplicate files, by computing the hash of all files.

    Args:
        root_path (str): root dir ie(where function start file search.)

    Returns:
        list[str]: all duplicate files.
    """
    mapping = dict()

    for _, _, files in os.walk(root_path):
        for file in files:
            checksum = hash_my_stuff(os.path.abspath(file))
            if checksum in mapping.keys():
                print(f"found duplicate of: {os.path.abspath(file)}")
            else:
                mapping[checksum] = os.path.abspath(file)

    return mapping

def delete(filename) -> int:
    """Deletes passed file, after verifies if deletion was successful.

    Args:
        filename (str): name of file to delete.

    Returns:
        int: status code.
    """
    status: int = 0
    print("deleting found duplicate.")
    os.remove(filename)

    status = os.path.exists(filename)

    if status != 0:
        print("removal failure :<")
        exit(1)

    return status

def main() -> int:
    """Entrypoint of program."""
    arg_parser = ARGUMENTPARSER()

    duplicate_files: dict[str] = find_files(arg_parser.argv.wsroot)

    print("These files are duplicates.")
    for file in duplicate_files.items():
        print(f"* {file[1]}")


if __name__ == "__main__":
    sys.exit(main())
