from enum import Enum
from typing import List

from utils.log_utils import log


class OpType(Enum):
    """
    任务类型枚举
    """

    INPUT = 'input'
    CLICK_IMG = 'click_img'
    CLICK_POSITION = 'click_position'
    OPERATION = 'operation'

    @classmethod
    def from_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"No enum member with value '{value}'")


class InputData:
    """
    字符串输入任务对象
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value


class ClickImgData:
    """
    点击图片任务对象
    """

    def __init__(self, value: str, confidence: float = 0.8):
        self.value = value
        self.confidence = confidence

    def __str__(self):
        return self.value + ' ' + str(self.confidence)


class ClickPositionData:
    """
    点击坐标任务对象
    """

    def __init__(self, position: (int, int)):
        self.x = position[0]
        self.y = position[1]

    def __str__(self):
        return f"({self.x}, {self.y})"


class Task:
    """
    任务对象，对应yaml配置文件中的一个任务
    """

    # 构造Task对象
    def __init__(self, name: str, type: OpType, data: (InputData | ClickImgData | ClickPositionData),
                 interval: int, turns: int, operations: List['Task']):
        self.name: str = name
        self.type: OpType = type
        self.turns: int = turns
        self.data: (InputData | ClickImgData | ClickPositionData) = data
        self.interval: int = interval
        # 子任务list
        self.operations: List['Task'] = operations

    @property
    def is_operation(self):
        return self.type == OpType.OPERATION


def build_task_tree(task_data: []) -> List[Task]:
    """
    递归构建任务列表，并配置默认参数
    :param task_data: 当前配置的任务列表
    :return: 任务树
    """
    if (task_data is None) or (len(task_data) == 0):
        return []

    ret: List[Task] = []
    for task_data_item in task_data:
        name: str = task_data_item.get('name', None)
        type: OpType = OpType.from_value(task_data_item.get('type', None))
        task_data_item_data: {} = task_data_item.get('data', None)
        data = None
        if task_data_item_data is not None:
            if type == OpType.INPUT:
                data = InputData(task_data_item_data)
            elif type == OpType.CLICK_IMG:
                if isinstance(task_data_item_data, str):
                    data = ClickImgData(task_data_item_data)
                else:
                    data = ClickImgData(task_data_item_data.get('value'), task_data_item_data.get('confidence', 0.8))
            elif type == OpType.CLICK_POSITION:
                data = ClickPositionData(task_data_item_data)
        interval = task_data_item.get('interval', 0.3)
        turns = task_data_item.get('turns', 1)
        operations = task_data_item.get('operations', None)
        ret.append(Task(name, type, data, interval, turns, build_task_tree(operations)))
    return ret


def print_task_tree(task_list: List[Task]):
    """
    递归打印任务
    :param task_list: 任务列表
    :return:
    """
    for task in task_list:
        if task.is_operation:
            log.info(f"Task: {task.type} {task.name}")
            print_task_tree(task.operations)
        else:
            log.info(f"Task: {task.type} {task.name} {task.data}")
