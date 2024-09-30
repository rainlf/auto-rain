from loguru import logger as log
from task.task_runner import TaskRunner

module = 'infosafe'
mission = 'session_handle'


task_runner = TaskRunner(module, mission)
task_runner.dry_run()
task_runner.run()
