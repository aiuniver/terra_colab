import os
import sys
import getopt
import argparse


from pathlib import Path


def _parse_argv(argv):
    print(argv)
    inputfile = ""
    outputfile = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("test.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("test.py -i <inputfile> -o <outputfile>")
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)


def _mount_google_drive(path: Path) -> bool:
    # print(path)
    return False


def init():
    print(_parse_argv(sys.argv[1:]))
    # print(Path().resolve())
    # print(os.path.abspath(os.getcwd()))
    if not _mount_google_drive(Path("/content/drive")):
        return
