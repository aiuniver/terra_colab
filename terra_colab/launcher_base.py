from typing import Optional, Any


class LauncherBase:
    def getup(self, dataset: Optional[Any] = None):
        print(f'Launcher getup with dataset "{dataset} -> {type(dataset)}"')
