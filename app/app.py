from run_captain import deploy_uat as deploy_uat
from run_captain import deploy_devb as deploy_devb
from run_infosafe import run_task as run_infosafe
from run_touchfish import run_task as run_touchfish

title = '''\
Auto Rain
0. touch fish
1. run captain uat
2. run captain devb
3. run infosafe
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
    '1': deploy_uat,
    '2': deploy_devb,
    '3': run_infosafe,
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
