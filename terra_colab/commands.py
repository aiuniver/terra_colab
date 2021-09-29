import os
import sys
import shutil
import getopt
import requests
import subprocess

from git import Repo
from enum import Enum
from dotenv import dotenv_values
from typing import Optional, List
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
    print(f"\033[1;31m{message}\033[0m")


def _parse_argv(argv) -> dict:
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


class WebServer:
    __env: EnvChoice
    __branch: Optional[str]
    __force: bool
    __path: Path
    __url: str = ""
    __email: str = ""
    __token: str = ""
    __auth_data: dict = {}

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
        self.__mount_google_drive()
        self.__download_gui()
        self.__prepare_data()

        print(
            f"\033[1;32mДля начала работы перейдите по следующей ссылке {self.__url}\033[0m"
        )
        try:
            subprocess.Popen(["make", "-C", Path(self.__path, TERRA_DIRECTORY)])
        except KeyboardInterrupt:
            sys.exit()

    def __str__(self):
        return f"""[TerraAI WebServer]
Env    : {self.__env}
Branch : {self.__branch}
Force  : {self.__force}
Path   : {self.__path}
URL    : {self.__url}
Email  : {self.__email}
Token  : {self.__token}"""

    def __auth(self):
        _env_file = Path(self.__path, TERRA_DIRECTORY, ENV_FILE)
        if _env_file.is_file():
            _config = dotenv_values(str(_env_file.absolute()))
            self.__url = _config.get("USER_URL", "")
            self.__email = _config.get("USER_EMAIL", "")
            self.__token = _config.get("USER_TOKEN", "")

        if not self.__email or not self.__token:
            self.__email = str(input(AUTH_EMAIL_LABEL))
            self.__token = str(input(AUTH_TOKEN_LABEL))

        try:
            _domain_prefix = "" if self.__env == EnvChoice.prod else f"{self.__env}."
            response = requests.post(
                f"{EXTERNAL_SERVER_API % _domain_prefix}/login/",
                json={"email": self.__email, "user_token": self.__token},
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
            raise WebServerException(data.get("error"))

        self.__url = data.get("data", {}).get("url", "")
        if not self.__url:
            raise WebServerException("Undefined URL to GUI")

        self.__auth_data = data.get("data", {})

    def __mount_google_drive(self):
        try:
            google_drive.mount(
                str(Path(self.__path, GOOGLE_DRIVE_DIRECTORY).absolute()),
                force_remount=self.__force,
            )
        except Exception as error:
            raise WebServerException(error)

    def __download_gui(self):
        _terra_path = Path(self.__path, TERRA_DIRECTORY)
        repo_kwargs = {}
        if self.__branch:
            repo_kwargs.update({"branch": self.__branch})
        if not _terra_path.is_dir() or self.__force:
            shutil.rmtree(_terra_path, ignore_errors=True)
            try:
                Repo.clone_from(TERRA_REPOSITORY, _terra_path, **repo_kwargs)
            except Exception as error:
                raise WebServerException(error)

    def __prepare_data(self):
        _terra_path = Path(self.__path, TERRA_DIRECTORY)
        for name, info in self.__auth_data.get("create", {}).items():
            with open(Path(_terra_path, info.get("name")), "w") as _file_ref:
                _file_ref.write(info.get("data"))

        with open(Path(self.__path, TERRA_DIRECTORY, ENV_FILE), "a") as _env_file_ref:
            _env_file_ref.write(f"USER_URL={self.__url}\n")
            _env_file_ref.write(f"USER_EMAIL={self.__email}\n")
            _env_file_ref.write(f"USER_TOKEN={self.__token}\n")


def web():
    kwargs = _parse_argv(sys.argv[1:])
    try:
        print(WebServer(**kwargs))
    except WebServerException as error:
        _print_error(error)
