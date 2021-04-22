import os
import shutil
import requests
import subprocess

from google.colab import drive
from typing import Optional, Any

COLAB_CONTENT_PATH = "/content"
COLAB_TERRA_GUI_PATH = f"{COLAB_CONTENT_PATH}/terra_gui"
COLAB_AUTH_URL = "http://terra.neural-university.ru/api/v1/login/"
COLAB_TERRA_GUI_GIT = "https://github.com/aiuniver/terra_gui.git"


class LauncherBase:
    """
    Класс для управления запуском веб-сервера
    """

    def __error(self, message: str):
        """
        Вывод ошибки пользователю
        :param message: str - Строка ошибки
        :return: None
        """
        print(f"\033[0;31m{message}\033[0m")

    def __auth(self) -> Optional[dict]:
        """
        Авторизация пользователя на стороне сервера terra_ai
        :return: dict
        """

        def __input(title: str) -> Optional[str]:
            value = input(title)
            if not value:
                return __input(title=title)
            return value

        email = __input("Введите E-mail: ")
        token = __input("Введите Token: ")

        try:
            response = requests.post(
                COLAB_AUTH_URL,
                data={"email": email, "user_token": token},
            )
            response.raise_for_status()
            return response.json()
        except Exception as error:
            self.__error(str(error))

    def __prepare(self, data: dict):
        """
        Подготовка необходимых файлов по полученным после авторизации данным
        :param data: dict - Словарь данных, которые вернула авторизация
        :return: None
        """
        for value in data.values():
            with open(value.get("name"), "w") as file:
                file.write(value.get("data"))

    def getup(self, dataset: Optional[Any] = None):
        """
        Запуск веб-сервера
        :param dataset: Optional[Any] - Экземпляр класса DTS, если необходимо запустить веб-сервер с собственным датасетом
        :return: None
        """
        if dataset:
            print(f'Launch with dataset "{str(dataset)} -> {type(dataset)}"')
        else:
            print("Launch without dataset")

        os.chdir(COLAB_CONTENT_PATH)

        response = self.__auth()
        if not response:
            return

        if not response.get("success"):
            self.__error(response.get("error"))
            return

        drive.mount(f"{COLAB_CONTENT_PATH}/drive")

        try:
            shutil.rmtree(COLAB_TERRA_GUI_PATH)
        except Exception:
            pass

        git_clone = subprocess.Popen(
            ["git", "clone", COLAB_TERRA_GUI_GIT, "./terra_gui"]
        )
        git_clone.wait()
        os.chdir(COLAB_TERRA_GUI_PATH)

        self.__prepare(response.get("data").get("create"))

        print(
            f'Для начала работы перейдите по следующей ссылке {response.get("data").get("url")}'
        )

        with subprocess.Popen(
            ["pip", "install", "-r", "./requirements/colab.txt"]
        ) as proc:
            print("proc:", proc)
            proc.wait()
            print("Complete")

        # pip_install = subprocess.Popen(["chmod", "400", "$(RSA_KEY)"])
        # print("pip_install:", pip_install)
        # pip_install.wait()

        """
chmod +x ./manage.py
./manage.py runserver 80 & ssh -i './$(RSA_KEY)' -o StrictHostKeyChecking=no -R $(PORT):localhost:80 $(TUNNEL_USER)
        """
