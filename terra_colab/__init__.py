from .launcher_base import LauncherBase

__version__ = "0.1"


launcher = LauncherBase()


def print_globals_keys():
    print(globals().keys())
