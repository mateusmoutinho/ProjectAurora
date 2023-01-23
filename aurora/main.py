
from aurora.entrys import get_inputs
from process import run_comand,kill_all_processes
from git import Repo
from os import getpid
from sys import exit









def main():
    inputs = get_inputs()
    repository_path = inputs['repository']
    time_wait = inputs['time']
    comand = inputs['comand']
     
    try:
        repo = Repo(repository_path)
    except:
        print('Invalid repository path. Exiting...')
        exit(1)
    try:
        run_comand(comand,time_wait,repo)
    except Exception as e:
        print('Exiting...')
        # kill the process
        kill_all_processes(getpid())
        exit(0)

if __name__ == '__main__':
    
    main()