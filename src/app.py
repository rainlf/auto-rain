from task.task_runner import TaskRunner

module = 'infosafe'
mission = 'handles'

task_runner = TaskRunner(module, mission)
task_runner.dry_run()
