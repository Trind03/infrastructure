import os
import subprocess
import sys

def run_cmd(cmd) -> int:
    popen: subprocess.Popen = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return popen.wait()


def findelements():
    """ Function for mapping all cpp & header files. """
    status = 0
    elements = []
    directory = os.path.abspath(os.getcwd())

    print("finding elements")

    for dir,folders,files in os.walk(directory):
        for file in files:
            if file.endswith(".cpp") or file.endswith(".h"):
                elements.append(os.path.join(dir, file))

    return status,elements if elements else 0,elements

def format_files(filename) -> int:
    print(f"Formatting: {filename}")
    status_code = run_cmd(["clang-format", "-i", filename])

    if status_code == 0:
        print(f"Formatted! {filename}")
        return 0
    print(f"Format failure! {filename}")
    return 1

def main() -> int:
    status, arr = findelements()
    if status != 0:
        return 1

    for filename in arr:
        status = format_files(filename)
        if status != 0:
            return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())