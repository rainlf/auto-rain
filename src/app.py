from task.task_runner import TaskRunner

module = 'infosafe'
mission = 'handle_20'


task_runner = TaskRunner(module, mission)
task_runner.run()
