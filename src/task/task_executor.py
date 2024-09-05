import time
from enum import Enum

import utils.file_utils as file_utils
import utils.gui_utils as gui_utils
from config.yaml_config import YamlConfig
from utils.log_utils import log


class OpType(Enum):
    CLICK = 'click'
    INPUT = 'input'


class TaskExecutor:
    """
    初始化配置文件和任务名称
    """

    def __init__(self, module_name: str, task_name: str):
        self.config = YamlConfig(file_utils.get_config_file_path(f'{module_name}.yml'))
        self.module_name = module_name
        self.task_name = task_name
        if task_name not in self.config.data:
            log.error(f"Task {task_name} not found in config file.")
            raise Exception(f"Task {task_name} not found in config file.")
        self.task_list = self.config.data[task_name]

    def execute(self):
        """
        开始执行任务
        :return:
        """
        for task in self.task_list:
            if 'operations' in task:
                for sub_task in task['operations']:
                    self.loop_task_until_success(sub_task)
            else:
                self.loop_task_until_success(task)

    def loop_task_until_success(self, task: {}) -> None:
        """
        循环执行任务直到成功
        :param task: 一个任务配置对象
        :return:
        """
        while True:
            log.info(f"[{task['op_type']}] [{task['op_name']}] '{task['data']}'")
            if self.dispatch_task(task):
                break
            time.sleep(1)
        if 'interval' in task:
            log.info(f"[{task['op_type']}] [{task['op_name']}] completed, sleep {task['interval']} seconds")
            time.sleep(task['interval'])

    def dispatch_task(self, tasks: {}) -> bool:
        """
        根据op_type分发任务
        :param tasks: 一个任务配置对象
        :return:
        """
        if 'op_type' not in tasks:
            log.error(f"Task type not found in task {tasks}")
            return False

        task_type = tasks['op_type']
        if task_type == OpType.CLICK.value:
            return self.do_click_task(tasks)
        elif task_type == OpType.INPUT.value:
            return self.do_input_task(tasks)
        else:
            log.error(f"Unknown task type {task_type}")
            return False

    def do_click_task(self, task: {}) -> bool:
        if 'data' not in task:
            log.error(f"Data not found in task {task}")
            return False
        return gui_utils.click(self.module_name, task['data'], task.get('confidence', 0.8))

    def do_input_task(self, task: {}) -> bool:
        if 'data' not in task:
            log.error(f"Data not found in task {task}")
            return False
        return gui_utils.write(task['data'])
