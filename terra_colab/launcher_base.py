import os

from typing import Optional, Any

from . import COLAB_CONTENT_PATH


class LauncherBase:
    """
    Класс для управления запуском веб-сервера
    """

    def __auth(self) -> dict:
        """
        Авторизация пользователя на стороне сервера terra_ai
        :return: dict
        """
        email = input("Введите E-mail:")
        token = input("Введите Token:")
        print(email)
        print(token)

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
        # try:
        #     response = auth()
        #     if not response.get("success"):
        #         error(response.get("error"))
        #     else:
        #         drive.mount("/content/drive")
        #     !rm -rf ./terra_gui
        #     !git clone https://github.com/aiuniver/terra_gui.git ./terra_gui &> /dev/null
        #     %cd ./terra_gui
        #     prepare(response.get("data").get("create"))
        #     print(f'Для начала работы перейдите по следующей ссылке {response.get("data").get("url")}')
        #     !make &> /dev/null
        # except requests.exceptions.ConnectionError as error:
        #     error("Ошибка соединения с сервером авторизации! Попробуйте позже...")
