import utils.file_utils as file_utils
from config.yaml_config import YamlConfig
from task.task_executor import TaskExecutor
from utils.log_utils import log

file: str = file_utils.get_file_path('captain.yml')
config: YamlConfig = YamlConfig(file)
task: TaskExecutor = TaskExecutor(config, 'task_publish')

log.info("-----------------")
task.execute()
