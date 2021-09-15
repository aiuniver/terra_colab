import os
import sys
import getopt

from git import Repo
from pathlib import Path
from google.colab import drive as google_drive


def _print_error(message: str):
    """
    Вывод ошибки
    """
    print(f"\033[1;31m{message}\033[0m")


def _parse_argv(argv) -> dict:
    """
    Получение аргуметов командной строки
    """
    opts = []
    try:
        opts, args = getopt.getopt(argv, "hb:f", ["help", "branch=", "force"])
    except getopt.GetoptError:
        pass

    print(opts)
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

    output = {
        "branch": None,
        "force": False,
    }
    for opt, arg in opts:
        if opt in ("-b", "--branch"):
            output.update({"branch": arg})
        if opt in ("-f", "--force"):
            output.update({"force": True})

    return output


def _mount_google_drive(path: Path) -> bool:
    """
    Подклчение GoogleDrive
    """
    try:
        google_drive.mount(str(path.absolute()))
        return True
    except Exception as error:
        _print_error(str(error))
        return False


def web():
    """
    Запуск пользовательского интерфейса в GoogleColab
    """
    kwargs = _parse_argv(sys.argv[1:])
    working_path = Path(os.path.abspath(os.getcwd()))

    # if not _mount_google_drive(Path(working_path, "drive")):
    #     return

    repo_kwargs = {}
    branch = kwargs.get("branch")
    if branch:
        repo_kwargs.update({"branch": branch})
    try:
        repo = Repo.clone_from(
            "https://github.com/aiuniver/terra_gui.git",
            Path(working_path, "terra"),
            **repo_kwargs,
        )
    except Exception as error:
        _print_error(str(error))
        sys.exit()

    print("sss")
