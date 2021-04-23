# from google.colab import drive
import os

from .launcher import launcher


def auth():
    os.environ["EMAIL"] = input("Введите E-mail: ")
    os.environ["TOKEN"] = input("Введите Token: ")
    # drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())


def gdmount():
    pass
