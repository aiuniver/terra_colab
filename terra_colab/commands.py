# from google.colab import drive
import os

from .launcher import launcher


def auth():
    email = input("Введите E-mail: ")
    token = input("Введите Token: ")
    os.system(
        f"""
        export EMAIL={email}
        export TOKEN={token}
    """
    )
    # drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())


def gdmount():
    pass
