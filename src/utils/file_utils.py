import os
from typing import Optional

# WORK_DIR: Optional[str] = None
WORK_DIR: Optional[str] = 'D:\\Users\\yhee\\Desktop\\auto-rain'


def get_work_dir() -> str:
    if WORK_DIR is not None:
        return WORK_DIR
    else:
        return os.getcwd()


def get_file_path(*path) -> str:
    return os.path.join(get_work_dir(), 'assert', *path)
