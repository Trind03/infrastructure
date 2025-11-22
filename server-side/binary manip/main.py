import sys
from binaryparser import parser
from file import filehandler

def main() -> int:
    print(filehandler.add_excention("file.txt", ".bin"))

    return 0


if __name__ == '__main__':
    sys.exit(main())
