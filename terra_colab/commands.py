import os
import sys

from pathlib import Path


def _mount_google_drive(path: Path) -> bool:
    # print(path)
    return False


def init():
    print(sys.argv)
    # print(Path().resolve())
    # print(os.path.abspath(os.getcwd()))
    if not _mount_google_drive(Path("/content/drive")):
        return
