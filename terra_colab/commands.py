import os
import sys
import argparse


from pathlib import Path


def _mount_google_drive(path: Path) -> bool:
    # print(path)
    return False


def init():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "counter", help="An integer will be increased by 1 and printed.", type=int
    )
    args = parser.parse_args()
    print(args.counter + 1)
    # print(Path().resolve())
    # print(os.path.abspath(os.getcwd()))
    if not _mount_google_drive(Path("/content/drive")):
        return
