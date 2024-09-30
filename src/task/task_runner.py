from loguru import logger as log
from task.task import Task, TaskType
from utils import file_utils, yaml_utils


class TaskRunner:
    def __init__(self, module: str, mission: str):
        self._module = module
        self._mission = mission
        self.tasks = self.__load_config()

    def __load_config(self):
        file = file_utils.get_config(self._module)
        log.debug(f"config file: {file}")
        config = yaml_utils.load_yaml(file)
        mission = config[self._mission]
        tasks = []
        for step in mission:
            data = mission[step]
            tasks.append(Task(step, data['name'], TaskType[data['type']], data['data'], data.get('config')))

        return tasks

    def dry_run(self):
        for task in self.tasks:
            log.info(f"task: {task}")
