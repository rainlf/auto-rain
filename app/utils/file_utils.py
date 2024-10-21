import os

IMAGE_DIR: str = os.path.join(os.path.dirname(os.getcwd()), 'assert', 'img')
CONFIG_DIR: str = os.path.join(os.path.dirname(os.getcwd()), 'assert', 'config')


def get_img(*path) -> str:
    return os.path.join(IMAGE_DIR, *path)


def get_config(*path) -> str:
    return os.path.join(CONFIG_DIR, *path) + '.yml'
