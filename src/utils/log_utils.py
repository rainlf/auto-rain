import loguru

LOG_FORMAT: str = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>|<level>{level: <8}</level>|<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"


def get_log():
    log = loguru.logger
    log.add("/tmp/logs/app_{time}.log", rotation="10 MB", retention="365 days", format=LOG_FORMAT, level="INFO")
    return log


log = get_log()
