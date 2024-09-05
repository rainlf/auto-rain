from task.task_executor import TaskExecutor
from utils.log_utils import log


module = 'captain'
task: TaskExecutor = TaskExecutor(module, 'task_publish')
log.info("-----------------")
task.execute()
