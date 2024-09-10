import time
from enum import Enum

import utils.file_utils as file_utils
import utils.gui_utils as gui_utils
from config.yaml_config import YamlConfig
from utils.log_utils import log


class OpType(Enum):
    CLICK = 'click'
    INPUT = 'input'
    CLICK_POSITION = 'click_position'


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
        执行任务入口
        :return:
        """
        for task in self.task_list:
            self.execute_task(task)

    def execute_task(self, task: {}):
        """
        执行单个任务
        如果任务包含operations字段，则递归执行
        否则执行loop_task_until_success
        :param task: 一个任务配置对象
        :return:
        """
        if 'operations' in task:
            for sub_task in task['operations']:
                self.execute_task(sub_task)
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
            if 'turns' in task:
                for i in range(task['turns']):
                    log.info(f"[{task['op_type']}] [{task['op_name']}] turn {i + 1}/{task['turns']}")
                    if self.dispatch_task(task):
                        break
            else:
                if self.dispatch_task(task):
                    break
            time.sleep(0.3)

        if 'interval' in task:
            log.info(f"[{task['op_type']}] [{task['op_name']}] completed, sleep {task['interval']} seconds")
            time.sleep(task['interval'])

    def dispatch_task(self, task: {}) -> bool:
        """
        根据op_type分发任务
        :param task: 一个任务配置对象
        :return:
        """
        if 'op_type' not in task:
            log.error(f"Task type not found in task {task}")
            return False
        if 'data' not in task:
            log.error(f"Data not found in task {task}")
            return False

        task_type = task['op_type']
        if task_type == OpType.CLICK.value:
            return self.do_click_task(task)
        elif task_type == OpType.INPUT.value:
            return self.do_input_task(task)
        elif task_type == OpType.CLICK_POSITION.value:
            return self.do_click_position_task(task)
        else:
            log.error(f"Unknown task type {task_type}")
            return False

    def do_click_task(self, task: {}) -> bool:
        return gui_utils.click(self.module_name, task['data'], confidence=task.get('confidence', 0.8))

    def do_input_task(self, task: {}) -> bool:
        return gui_utils.write(task['data'])

    def do_click_position_task(self, task: {}) -> bool:
        return gui_utils.click_position(task['data'][0], task['data'][1])
