import time
from enum import Enum, auto
from typing import Dict, List

import keyboard
from loguru import logger as log

from utils import file_utils
from utils import gui_utils

running = True


def listen_stop():
    global running
    keyboard.wait('F10')
    print("F10 pressed, stop...")
    running = False


class TaskType(Enum):
    OPEN_URL = auto()
    CLICK_IMG = auto()
    CLICK_TEXT = auto()
    KEYBOARD_INPUT = auto()
    SUB_MISSIONS = auto()


class Task:
    def __init__(self, module: str, step: str, name: str, type: TaskType, data: str, config: Dict):
        self._module = module
        self._step = step
        self._name = name
        self._type = type
        self._data = data
        self._config = config
        if self._config is None:
            self._config = {}
        self._default_sleep = 0.5
        self._sleep = self._config.get('sleep', self._default_sleep)

    def __str__(self):
        return f"step: {self._step}, name: {self._name}, type: {self._type}, data: {self._data}, config: {self._config}"

    def dry_run(self):
        log.info(f"task: {self}")

    def run(self) -> bool:
        """
        任务执行实现，根据不同的任务类型执行具体的操作
        :return: 是否执行成功
        """
        log.info(f"task: {self}")

        try:
            if self._type == TaskType.OPEN_URL:
                gui_utils.open_url(self._data)
            elif self._type == TaskType.CLICK_IMG:
                img = file_utils.get_img(self._module, self._data)
                condition = self._config.get('condition', 0.8)
                gui_utils.click_img(img, condition)
            elif self._type == TaskType.CLICK_TEXT:
                gui_utils.click_text(self._data)
            elif self._type == TaskType.KEYBOARD_INPUT:
                gui_utils.write(self._data)
            elif self._type == TaskType.SUB_MISSIONS:
                missions = self._data
                times = self._config.get('times', 1)
                self.handle_sub_tasks(missions, times)
            else:
                log.error(f"unknown task type: {self._type}")
        except Exception as e:
            log.error(f"task run failed: {e}")
            return False
        finally:
            time.sleep(self._sleep)
        return True

    def handle_sub_tasks(self, missions, times) -> bool:
        for _ in range(times):
            if running:
                log.info(f"do sub mission, time: {_ + 1}/{times}")
                tasks = build_tasks_from_missions(self._module, missions)
                i = 0
                while running and i < len(tasks):
                    print(f"TEST2: {running}")
                    task = tasks[i]
                    if task.run():
                        i += 1
        return True


def build_tasks_from_missions(module, missions) -> List[Task]:
    tasks = []
    for name in missions:
        mission = missions[name]
        tasks.append(
            Task(module, name, mission['name'], TaskType[mission['type']], mission['data'], mission.get('config')))
    return tasks
