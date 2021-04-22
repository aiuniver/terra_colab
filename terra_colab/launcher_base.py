class LauncherBase:
    def getup(self, dataset: str = ""):
        print(f'Launcher getup with dataset "{dataset}[type={type(dataset)}]"')
        dataset = globals().get(dataset, None)
        if dataset:
            print("Dataset is undefined")
        else:
            print("Dataset loaded:", dataset, type(dataset))
