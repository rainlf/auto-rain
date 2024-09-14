from enum import Enum
from typing import List


class OpType(Enum):
    """
    任务类型枚举
    """

    INPUT = 'input'
    CLICK = 'click_img'
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


class ClickImgData:
    """
    点击图片任务对象
    """

    def __init__(self, value: str, confidence: float = 0.8):
        self.value = value
        self.confidence = confidence


class ClickPositionData:
    """
    点击坐标任务对象
    """

    def __init__(self, position: (int, int)):
        self.x = position[0]
        self.y = position[1]


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
        self.interval = interval
        # 子任务list
        self.operations = operations

    @property
    def is_operation(self):
        return self.type == OpType.OPERATION
