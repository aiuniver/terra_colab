from typing import Optional, Any


class LauncherBase:
    dataset: Optional[Any] = None

    def getup(self):
        print("Launcher getup")
