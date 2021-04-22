from os import chdir
from typing import Optional, Any


class LauncherBase:
    def getup(self, dataset: Optional[Any] = None):
        if dataset:
            print(f'Launch with dataset "{dataset} -> {type(dataset)}"')
        else:
            print("Launch without dataset")

        chdir
        %cd / content