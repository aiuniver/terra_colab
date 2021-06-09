class TerraProject:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.__class__}: {self.name}"
