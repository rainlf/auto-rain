from task.task_runner import TaskRunner


def deploy_uat():
    module = 'captain'
    mission = 'task_publish_uat'

    task_runner = TaskRunner(module, mission)
    task_runner.run()


def deploy_devb():
    print('start run task: run captain')
    module = 'captain'
    mission = 'task_publish_devb'

    task_runner = TaskRunner(module, mission)
    task_runner.run()
