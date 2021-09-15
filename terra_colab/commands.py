import os
import sys
import shutil
import getopt
import requests

from git import Repo
from pathlib import Path
from google.colab import drive as google_drive


DEFAULT_ENV = "prod"

TERRA_REPOSITORY = "https://github.com/aiuniver/terra_gui.git"
EXTERNAL_SERVER_API = "http://%sterra.neural-university.ru/api/v1"

GOOGLE_DRIVE_DIRECTORY = "drive"
TERRA_DIRECTORY = "terra"

AUTH_EMAIL_LABEL = "Введите E-mail: "
AUTH_TOKEN_LABEL = "Введите Token: "


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
        opts, args = getopt.getopt(argv, "he:b:f", ["help", "env=", "branch=", "force"])
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
    -e, --env
            Используемое окружение на удаленном сервере
    -b, --branch
            Ветка в репозитории пользовательского интерфейса
    -f, --force
            Принудительные:
            - авторизация пользователя
            - монтирование GoogleDrive
            - клонирование репозитория"""
        )
        sys.exit()

    output = {
        "env": DEFAULT_ENV,
        "branch": None,
        "force": False,
    }
    for opt, arg in opts:
        if opt in ("-e", "--env"):
            output.update({"env": arg})
        elif opt in ("-b", "--branch"):
            output.update({"branch": arg})
        elif opt in ("-f", "--force"):
            output.update({"force": True})

    return output


def _auth(env: str = None) -> bool:
    if env == DEFAULT_ENV:
        env = None
    _domain_prefix = f"{env}." if env else ""
    _email = str(input(AUTH_EMAIL_LABEL))
    _token = str(input(AUTH_TOKEN_LABEL))

    print(f"{EXTERNAL_SERVER_API % _domain_prefix}/login/")
    response = requests.post(
        f"{EXTERNAL_SERVER_API % _domain_prefix}/login/",
        json={"email": _email, "user_token": _token},
    )
    if not response.ok:
        _print_error("Ошибка запроса авторизации! Попробуйте позже...")
        return False

    print(response.content)
    print(response.json())

    return False


def _mount_google_drive(path: Path, force: bool = False) -> bool:
    """
    Подклчение GoogleDrive
    """
    try:
        google_drive.mount(str(path.absolute()), force_remount=force)
        return True
    except Exception as error:
        _print_error(str(error))
        return False


def web():
    """
    Запуск пользовательского интерфейса в GoogleColab
    """
    kwargs = _parse_argv(sys.argv[1:])
    _env = kwargs.get("env")
    _branch = kwargs.get("branch")
    _force = kwargs.get("force", False)
    _working_path = Path(os.path.abspath(os.getcwd()))

    if not _auth(_env):
        return

    if not _mount_google_drive(
        Path(_working_path, GOOGLE_DRIVE_DIRECTORY), force=_force
    ):
        return

    repo_path = Path(_working_path, TERRA_DIRECTORY)
    repo_kwargs = {}
    if _branch:
        repo_kwargs.update({"branch": _branch})
    if not repo_path.is_dir() or _force:
        shutil.rmtree(repo_path, ignore_errors=True)
        try:
            Repo.clone_from(TERRA_REPOSITORY, repo_path, **repo_kwargs)
        except Exception as error:
            _print_error(str(error))
            sys.exit()

    print("Complete")
