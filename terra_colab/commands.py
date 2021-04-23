# from google.colab import drive
import os
import subprocess

from .launcher import launcher


def auth():
    email = input("Введите E-mail: ")
    token = input("Введите Token: ")
    ddd = subprocess.Popen(f"export EMAIL={email}; export TOKEN={token}")
    print(ddd)
    ddd.wait()
    # drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())


def gdmount():
    pass
