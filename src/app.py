from task.task_executor import TaskExecutor
from config.yaml_config import YamlConfig
import utils.file_utils as file_utils
from task.task import *

module = 'captain'
# task: TaskExecutor = TaskExecutor(module, 'task_publish')
task: TaskExecutor = TaskExecutor(module, 'task_publish_b')

# task.execute()
#
# module = 'qconfig'
# task: TaskExecutor = TaskExecutor(module, 'publish')
# task.execute()


print_task_tree(task.task_list)
