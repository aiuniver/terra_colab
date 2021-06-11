import os
import importlib.util

from typing import Dict

from tensorflow.keras.models import Model, load_model
from tensorflow.python.keras.engine.functional import Functional


TERRA_AI_PATH = "/content/drive/MyDrive/TerraAI"


class TerraProject:
    name: str
    h5: Dict[str, Functional]
    model: Model

    def __init__(self, name: str):
        self.name = name
        self.h5 = {}
        self.model = None
        try:
            for item in os.listdir(self.project_path):
                if item.endswith(".h5"):
                    name = item.split(".")
                    name.pop()
                    self.h5.update(
                        {name.pop(): load_model(os.path.join(self.project_path, item))}
                    )
                if item.endswith(".py"):
                    self.model = self.load_keras(os.path.join(self.project_path, item))
        except FileNotFoundError as error:
            print(f"Не удалось прочитать проект «{self.name}»")

    def __str__(self):
        return f"""<{self.__class__.__name__}> {self.name}
h5: {self.h5}
model: {self.model}"""

    def __repr__(self):
        return self.__str__()

    @property
    def project_path(self) -> str:
        return os.path.join(TERRA_AI_PATH, "projects", self.name)

    def load_keras(self, filepath: str) -> Model:
        spec = importlib.util.spec_from_file_location("keras", filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.model
