import time
from enum import Enum, auto
from typing import Dict

from loguru import logger as log

from utils import gui_utils


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

    def dry_run(self):
        log.info(f"task: {self}")

    def run(self) -> bool:
        log.info(f"task: {self}")
        if self._config is None:
            self._config = {}
        try:
            if self._type == TaskType.OPEN_URL:
                gui_utils.open_url(self._data)
            elif self._type == TaskType.CLICK_IMG:
                gui_utils.click_img(self._data, self._config.get('confidence', 0.8))
            elif self._type == TaskType.CLICK_TEXT:
                gui_utils.click_text(self._data)
            elif self._type == TaskType.KEYBOARD_INPUT:
                gui_utils.write(self._data)
            else:
                log.error(f"unknown task type: {self._type}")

            time.sleep(self._config.get('sleep', 0.1))
        except Exception as e:
            log.error(f"task run failed: {e}")
            return False

        return True
