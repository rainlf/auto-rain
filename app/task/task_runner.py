from loguru import logger as log

from task.task import Task, build_tasks_from_missions
from utils import file_utils, yaml_utils
import task.task_switch as task_switch


class TaskRunner:
    def __init__(self, module: str, mission: str):
        self._module = module
        self._mission = mission

        self.tasks = self.__load_config()

    def __load_config(self) -> list[Task]:
        """
        根据配置的missions构建执行任务需要的tasks
        :return:
        """
        file = file_utils.get_config(self._module)
        log.info(f"config file: {file}")
        config = yaml_utils.load_yaml(file)
        mission = config[self._mission]
        return build_tasks_from_missions(self._module, mission)

    def dry_run(self):
        for task in self.tasks:
            task.dry_run()

    def run(self):
        """
        按序执行任务，任务执行失败时继续执行本次任务，直到成功
        """
        stop = task_switch.open_switch()
        i = 0
        while task_switch.running and i < len(self.tasks):
            task = self.tasks[i]
            if task.run():
                i += 1
        stop.join()