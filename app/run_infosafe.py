from task.task_runner import TaskRunner


def run_task():
    print('start run task: run infosafe')
    module = 'infosafe'
    mission = 'handles'

    task_runner = TaskRunner(module, mission)
    task_runner.run()


if __name__ == '__main__':
    run_task()
