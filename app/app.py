from run_captain import run_task as run_captain
from run_captain2 import run_task as run_captain2
from run_captain3 import run_task as run_captain3
from run_infosafe import run_task as run_infosafe
from run_touchfish import run_task as run_touchfish

title = '''\
Auto Rain
0. touch fish
1. run captain
2. run infosafe
3. run captain, connect to idev
4. run captain, open public prod
e. exit
Please select an option: \
'''

running = True


def exit_app():
    global running
    running = False
    print("option e pressed, exit...")


handle_map = {
    '0': run_touchfish,
    '1': run_captain,
    '2': run_infosafe,
    '3': run_captain2,
    '4': run_captain3,
    'e': exit_app,
}

if __name__ == '__main__':
    while running:
        option = input(title)
        handle = handle_map.get(option)
        if handle:
            handle()
        else:
            print("Invalid option: ", option)
            continue
