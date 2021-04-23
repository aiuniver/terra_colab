from google.colab import drive
from .launcher import launcher


def auth2shell():
    drive.mount("/content/drive")
    # launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    # print(globals().keys())
