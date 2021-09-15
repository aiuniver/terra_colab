import os
import sys
import shutil
import getopt
import requests

from git import Repo
from enum import Enum
from typing import Union, Optional, List
from pathlib import Path
from google.colab import drive as google_drive


ENV_FILE = ".env"

TERRA_REPOSITORY = "https://github.com/aiuniver/terra_gui.git"
EXTERNAL_SERVER_API = "http://%sterra.neural-university.ru/api/v1"

GOOGLE_DRIVE_DIRECTORY = "drive"
TERRA_DIRECTORY = "terra"

AUTH_EMAIL_LABEL = "Введите E-mail: "
AUTH_TOKEN_LABEL = "Введите Token: "


class WebServerException(Exception):
    pass


class EnvChoice(str, Enum):
    prod = "prod"
    dev = "dev"

    @staticmethod
    def values() -> List[str]:
        return list(map(lambda item: item.name, EnvChoice))


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
        "env": EnvChoice.prod.value,
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


class WebServer:
    __env: EnvChoice
    __branch: Optional[str]
    __force: bool
    __path: Path

    def __init__(self, **kwargs):
        try:
            self.__env = EnvChoice[kwargs.get("env", "prod")]
        except KeyError:
            raise WebServerException(
                f"Неверное значение типа окружения: возможные варианты {EnvChoice.values()}"
            )
        self.__branch = kwargs.get("branch")
        self.__force = kwargs.get("force", False)
        self.__path = Path(os.path.abspath(os.getcwd()))
        self.__auth()

    def __str__(self):
        return f"""[TerraAI WebServer]
 Env    : {self.__env}
 Branch : {self.__branch}
 Force  : {self.__force}
 Path   : {self.__path}"""

    def __auth(self):
        _env_file = Path(self.__path, TERRA_DIRECTORY, ENV_FILE)
        if _env_file.is_file() and not self.__force:
            return

        _domain_prefix = "" if self.__env == EnvChoice.prod else f"{self.__env}s."
        _email = str(input(AUTH_EMAIL_LABEL))
        _token = str(input(AUTH_TOKEN_LABEL))

        try:
            response = requests.post(
                f"{EXTERNAL_SERVER_API % _domain_prefix}/login/",
                json={"email": _email, "user_token": _token},
            )
        except Exception as error:
            raise WebServerException(error)

        if not response.ok:
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as error:
                raise WebServerException(error)

        data = response.json()
        if not data.get("success"):
            _print_error(str(data.get("error")))
            return False

        files = data.get("data", {}).get("create", {})
        for name, info in files.items():
            with open(Path(path, info.get("name")), "w") as file:
                file.write(info.get("data"))

        return {
            "TERRA_GUI_URL": data.get("data", {}).get("url", ""),
            "USER_EMAIL": _email,
            "USER_TOKEN": _token,
        }


def web():
    kwargs = _parse_argv(sys.argv[1:])
    try:
        print(WebServer(**kwargs))
    except WebServerException as error:
        _print_error(error)

    # _env = kwargs.get("env")
    # _branch = kwargs.get("branch")
    # _force = kwargs.get("force", False)
    # _working_path = Path(os.path.abspath(os.getcwd()))
    # _terra_path = Path(_working_path, TERRA_DIRECTORY)
    #
    # _auth_data = _auth(_terra_path, _env, _force)
    # if not _auth_data:
    #     return
    #
    # if not _mount_google_drive(Path(_working_path, GOOGLE_DRIVE_DIRECTORY), _force):
    #     return
    #
    # repo_kwargs = {}
    # if _branch:
    #     repo_kwargs.update({"branch": _branch})
    # if not _terra_path.is_dir() or _force:
    #     shutil.rmtree(_terra_path, ignore_errors=True)
    #     try:
    #         Repo.clone_from(TERRA_REPOSITORY, _terra_path, **repo_kwargs)
    #     except Exception as error:
    #         _print_error(str(error))
    #         sys.exit()
    #
    # if isinstance(_auth_data, dict):
    #     print("here")
    #
    # print("Complete")
