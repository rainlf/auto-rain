import time

from loguru import logger as log

from task.task import Task, TaskType
from utils import file_utils, yaml_utils


class TaskRunner:
    def __init__(self, module: str, mission: str):
        self._module = module
        self._mission = mission
        self.tasks = self.__load_config()
        self.default_sleep = 0.3

    def __load_config(self):
        file = file_utils.get_config(self._module)
        log.info(f"config file: {file}")
        config = yaml_utils.load_yaml(file)
        mission = config[self._mission]
        tasks = []
        for step in mission:
            data = mission[step]
            tasks.append(Task(self._module, step, data['name'], TaskType[data['type']], data['data'], data.get('config')))
        return tasks

    def dry_run(self):
        for task in self.tasks:
            task.dry_run()

    def run(self):
        i = 0
        while i < len(self.tasks):
            task = self.tasks[i]
            if task.run():
                i += 1
            time.sleep(self.default_sleep)
