""" Application for iterating reqursavly thro an library,
of photos and remove or point out duplicates"""

import argparse
import sys
import os
import hashlib

class ARGUMENTPARSER:
    """ Program spesific wrapper around argparse. """
    def __init__(self):
        self.parser = argparse.ArgumentParser("photorm")
        self.parser.add_argument("-r","--root",
                                 action="store_true",dest="Root directory of search.")

        self.parser.add_argument("-t","--terminate-them",action="store_true",
                                 dest="removes duplicate photos uppon descovery")

        self.processed_arguments = self.parser.parse_args(sys.argv[1:])


def hash_my_stuff(filename,algoithm="sha256",read_block_size=128):
    composite = hashlib.new(algoithm)
    try:
        with open(filename,"rb") as file:
            while chunk := file.read(read_block_size):
                composite.update(chunk)
        return composite.hexdigest()
    except Exception as error:
        print(error)


def main() -> int:
    """ Entrypoint of program. """
    Argparser = ARGUMENTPARSER()
    duplicate_photos = []
    mapping = dict()

    for current_dir,folders,files in os.walk(os.getcwd()):
        for file in files:
            hash = hash_my_stuff(os.path.abspath(file))
            if hash not in mapping.keys():
                mapping[hash] = os.path.abspath(file)
            else:
                print(f"found duplicate of: {os.path.abspath(file)}")



if __name__ == "__main__":
    sys.exit(main())
