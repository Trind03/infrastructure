""" Application for iterating reqursavly thro an library,
of photos and remove or point out duplicates"""
#!
import argparse
import sys
import os
import imagehash

class ARGUMENTPARSER:
    """ Program spesific wrapper around argparse. """
    def __init__(self):
        self.parser = argparse.ArgumentParser("photorm")
        self.parser.add_argument("-r","--root",
                                 action="store_true",dest="Root directory of search.")

        self.parser.add_argument("-t","--terminate-them",action="store_true",
                                 dest="removes duplicate photos uppon descovery")

        self.processed_arguments = self.parser.parse_args(sys.argv[1:])





def main() -> int:
    """ Entrypoint of program. """
    Argparser = ARGUMENTPARSER()
    duplicate_photos = []
    mapping = dict()

    # for current_dir,folders,files in os.walk(Argparser.parser.parse_args.root):
    print(Argparser.processed_arguments.root)


if __name__ == "__main__":
    sys.exit(main())
