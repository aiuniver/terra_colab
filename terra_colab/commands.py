from . import launcher


def getup(*args, **kwargs):
    print(args)
    print(kwargs)
    launcher.getup()
