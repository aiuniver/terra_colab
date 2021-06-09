import os

from tensorflow.keras.models import Model


TERRA_AI_PATH = "/content/drive/MyDrive/TerraAI"


class TerraProject:
    name: str = ""
    h5: list = []
    model: Model = None
    keras: str = ""

    def __init__(self, name: str):
        self.name = name
        for item in os.listdir(os.path.join(self.project_path, self.name)):
            print(item)

    def __str__(self):
        return f"<{self.__class__.__name__}> {self.name}"

    def __repr__(self):
        return self.__str__()

    @property
    def project_path(self) -> str:
        return os.path.join(TERRA_AI_PATH, "projects")
