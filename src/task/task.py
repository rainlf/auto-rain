from enum import Enum, auto
from typing import Dict


class TaskType(Enum):
    OPEN_URL = auto()
    CLICK_IMG = auto()
    CLICK_TEXT = auto()
    KEYBOARD_INPUT = auto()


class Task:
    def __init__(self, step: str, name: str, type: TaskType, data: str, config: Dict):
        self._step = step
        self._name = name
        self._type = type
        self._data = data
        self._config = config

    def __str__(self):
        return f"step: {self._step}, name: {self._name}, type: {self._type}, data: {self._data}, config: {self._config}"
