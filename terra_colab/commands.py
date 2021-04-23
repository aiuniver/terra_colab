# from google.colab import drive
import os
import subprocess

from .launcher import launcher


def auth():
    email = input("Введите E-mail: ")
    token = input("Введите Token: ")
    subprocess.call(f"EMAIL={email}; TOKEN={token}")
    # drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())


def gdmount():
    pass
