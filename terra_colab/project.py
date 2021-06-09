class TerraProject:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        print(f"{self.__class__}: {self.name}")
