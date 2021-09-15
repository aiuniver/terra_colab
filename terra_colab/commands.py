import os
import sys
import getopt

from pathlib import Path
from google.colab import drive as google_drive


def _parse_argv(argv) -> dict:
    opts = []
    try:
        opts, args = getopt.getopt(argv, "hb:", ["help", "branch="])
    except getopt.GetoptError:
        pass

    if len(list(filter(lambda opt: opt[0] in ("-h", "--help"), opts))):
        print(
            """NAME
    tc-web - Запуск пользовательского интерфейса TerraAI в GoogleColab

SYNOPSIS
    tc-web [OPTION]...

OPTIONS
    -h, --help
            Показать эту документацию
    -b, --branch
            Ветка в репозитории пользовательского интерфейса"""
        )
        sys.exit()

    output = {}
    for opt, arg in opts:
        if opt in ("-b", "--branch"):
            output.update({"branch": arg})

    return output


def _mount_google_drive(path: Path) -> bool:
    google_drive.mount(str(path.absolute()))
    return False


def web():
    kwargs = _parse_argv(sys.argv[1:])
    destination = Path(os.path.abspath(os.getcwd()))

    # Подклчение GoogleDrive
    if not _mount_google_drive(Path(destination, "drive")):
        return
