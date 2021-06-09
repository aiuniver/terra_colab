import os
import json

from typing import List

from tensorflow.keras.models import Model


TERRA_AI_PATH = "/content/drive/MyDrive/TerraAI"


class TerraProject:
    name: str = ""
    h5: List[str] = []
    model: Model = None
    config: dict = {}

    def __init__(self, name: str):
        self.name = name
        try:
            for item in os.listdir(self.project_path):
                if item.endswith(".h5"):
                    self.h5.append(item)
                if item.endswith(".conf"):
                    self.config = json.load(os.path.join(self.project_path, item))
                if item.endswith(".py"):
                    print("Create model from keras.py")
        except FileNotFoundError as error:
            print(f"Проект «{self.name}» не существует")

    def __str__(self):
        return f"<{self.__class__.__name__}> {self.name}"

    def __repr__(self):
        return self.__str__()

    @property
    def project_path(self) -> str:
        return os.path.join(TERRA_AI_PATH, "projects", self.name)
