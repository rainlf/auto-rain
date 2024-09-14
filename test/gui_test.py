from typing import Union

def process_data(data: Union[int, str, list]) -> None:
    if isinstance(data, int):
        print(f"处理整数: {data}")
    elif isinstance(data, str):
        print(f"处理字符串: {data}")
    elif isinstance(data, list):
        print(f"处理列表: {data}")

# 或者使用管道符号（Python 3.10+）
def process_data_v2(data: int | str | list) -> None:
    if isinstance(data, int):
        print(f"处理整数: {data}")
    elif isinstance(data, str):
        print(f"处理字符串: {data}")
    elif isinstance(data, list):
        print(f"处理列表: {data}")

# 测试函数
process_data(42)
process_data("Hello")
process_data([1, 2, 3])

process_data_v2(42)
process_data_v2("Hello")
process_data_v2([1, '1234', 3])

