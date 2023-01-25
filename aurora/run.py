

from aurora.entrys import get_inputs
from aurora.execution import exec_repository_actions,kill_all_process
from os import getpid
from sys import exit





def main():
    try:
        inputs = get_inputs()
    except Exception as e:
        print('Exiting...')
        exit(1)

    repository_path = inputs['repository']
    time_wait = inputs['time']
    comand = inputs['comand']
    exec_repository_actions(comand,time_wait,repository_path)


if __name__ == '__main__':
    
    main()