class TerraProject:
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"<{self.__class__.__name__}> {self.name}"

    def __repr__(self):
        return self.__str__()
