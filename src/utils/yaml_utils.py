from typing import Dict

import yaml


def load_yaml(file: str) -> Dict:
    with open(file, 'r', encoding='utf-8-sig') as file:
        return yaml.safe_load(file)
