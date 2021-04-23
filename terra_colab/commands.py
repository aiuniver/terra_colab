from google.colab import drive
from .launcher import launcher


def auth2shell():
    email = input("Введите E-mail: ")
    token = input("Введите Token: ")
    drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())
