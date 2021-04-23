from .launcher import launcher


def auth2shell():
    launcher.auth()
    # launcher = Launcher()
    # print(launcher)
    print(globals().keys())
