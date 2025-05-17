""" Application for iterating reqursavly thro an library,
of photos and remove or point out duplicates"""

import argparse
import sys
from os import getcwd, walk, path
import hashlib

class ARGUMENTPARSER:
    """ Program spesific wrapper around argparse. """
    def __init__(self):
        self.root_path = None

        self.parser = argparse.ArgumentParser("photorm")

        self.parser.add_argument("-","--kill",action="store_true",
                                 help="removes duplicate photos uppon descovery")

        self.parser.add_argument("--wsroot",type=str,
                            help="defines starting point for search",default=getcwd())

        self.argv = self.parser.parse_args(sys.argv[1:])


def hash_my_stuff(filename,algoithm="sha256",read_block_size=128):
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
        with open(filename,"rb") as file:
            while chunk := file.read(read_block_size):
                composite.update(chunk)
        return composite.hexdigest()

    except Exception as error:
        print(error)

def find_files(root_path) -> list[str]:
    """Find all duplicate files, by computing the hash of all files.

    Args:
        root_path (str): root dir ie(where function start file search.) 

    Returns:
        list[str]: all duplicate files.
    """
    duplicate_photos = []
    mapping = dict()

    for _,_,files in walk(root_path):
        for file in files:
            checksum = hash_my_stuff(path.abspath(file))
            if checksum not in mapping.keys():
                mapping[checksum] = path.abspath(file)
            else:
                print(f"found duplicate of: {path.abspath(file)}")

    return duplicate_photos


def main() -> int:
    """ Entrypoint of program. """
    arg_parser = ARGUMENTPARSER()

    duplicate_files: list[str] = find_files(arg_parser.argv.wsroot)

    print("These files are duplicates.")
    for file in duplicate_files:
        print(f"* {file}")


if __name__ == "__main__":
    sys.exit(main())
