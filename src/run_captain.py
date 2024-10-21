from task.task_runner import TaskRunner

module = 'captain'
mission = 'task_publish_b'

task_runner = TaskRunner(module, mission)
task_runner.run()
