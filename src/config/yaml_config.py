import os
import yaml


class YamlConfig:
    def __init__(self, file_path: str):
        self.file_path: str = file_path
        self.data: dict = {}
        self.__load_data()

    def __load_data(self):
        if self.file_path is None:
            return
        if not os.path.exists(self.file_path):
            return

        with open(self.file_path, 'r', encoding='utf-8-sig') as file:
            self.data = yaml.safe_load(file)

