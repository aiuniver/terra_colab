import os
import sys
import getopt

from git import Repo
from pathlib import Path
from google.colab import drive as google_drive


def _parse_argv(argv) -> dict:
    """
    Получение аргуметов командной строки
    """
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
    """
    Подклчение GoogleDrive
    """
    try:
        google_drive.mount(str(path.absolute()))
        return True
    except Exception as error:
        print(f"\033[1;31m{error}\033[0m")
        return False


def web():
    """
    Запуск пользовательского интерфейса в GoogleColab
    """
    kwargs = _parse_argv(sys.argv[1:])
    working_path = Path(os.path.abspath(os.getcwd()))

    # if not _mount_google_drive(Path(working_path, "drive")):
    #     return

    repo = Repo.clone_from(
        "https://github.com/aiuniver/terra_gui.git",
        Path(working_path, "terra"),
        branch=kwargs.get("branch", "main"),
    )
    assert not repo.bare
