from task.task_runner import TaskRunner


def run_task():
    module = 'infosafe'
    mission = 'handles'

    task_runner = TaskRunner(module, mission)
    task_runner.run()


if __name__ == '__main__':
    run_task()
