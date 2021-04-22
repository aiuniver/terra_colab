from typing import Optional, Any


class LauncherBase:
    dataset: Optional[Any] = None

    def getup(self):
        print(dir(self))
        print(self.dataset)
        print(type(self.dataset))
        # print(f'Launcher getup with dataset "{dataset}[type={type(dataset)}]"')
        # dataset = globals().get(dataset, None)
        # if dataset:
        #     print("Dataset is undefined")
        # else:
        #     print("Dataset loaded:", dataset, type(dataset))
