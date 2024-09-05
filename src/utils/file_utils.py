import os

# WORK_DIR: str = '.'
WORK_DIR: str = 'D:\\Users\\yhee\\Desktop\\auto-rain'

ASSERT_DIR: str = os.path.join(WORK_DIR, 'assert')
CONFIG_DIR: str = os.path.join(WORK_DIR, 'config')


def get_work_dir() -> str:
    if WORK_DIR is not None:
        return WORK_DIR
    else:
        return os.getcwd()


def get_assert_file_path(*path) -> str:
    return os.path.join(ASSERT_DIR, *path)


def get_config_file_path(*path) -> str:
    return os.path.join(CONFIG_DIR, *path)

