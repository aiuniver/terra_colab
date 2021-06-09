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
                    with open(os.path.join(self.project_path, item), "r") as config_ref:
                        self.config = json.load(config_ref)
                if item.endswith(".py"):
                    pass
        except FileNotFoundError as error:
            print(f"Проект «{self.name}» не существует")

    def __str__(self):
        return f"""<{self.__class__.__name__}> {self.name}
    h5: {self.h5}
    model: {self.model}
    config: {self.config}
"""

    def __repr__(self):
        return self.__str__()

    @property
    def project_path(self) -> str:
        return os.path.join(TERRA_AI_PATH, "projects", self.name)
