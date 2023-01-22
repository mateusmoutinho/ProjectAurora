from cli_args_system import Args
from git import Repo
from os import getcwd,system
from sys import exit

import time
import threading

def check_for_updates(repo:Repo)->bool:
    """Check if the local repo is up to date with the remote repo."""
    current_hash = repo.head.object.hexsha
    origin = repo.remotes.origin
    origin.fetch()
    try:
        remote_hash = origin.refs.main.commit.hexsha
    except:
        remote_hash = origin.refs.master.commit.hexsha
    return current_hash != remote_hash


def pull(repo:Repo):
    """comandute pull on the repo"""
    origin = repo.remotes.origin
    origin.pull()


def get_inputs()->dict:
    """Get the inputs from the user."""
    args = Args()
    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()
    comand = args.flags_content('comand','c','comand')
    comand = ' '.join(comand.flags())

    time = args.flag_str('time','t','time')
    if not time:
        time = 10
    else:
        try:
            time = int(time)     
        except:
            print('Invalid time specified. Exiting...')
            exit(1)

    if not comand:
        print('No comand specified. Exiting...')
        exit(1)
    return {
        'repository':repo,
        'comand':comand,
        'time':time
    }    


def run_comand(comand:str,time_wait:int,repo:Repo):
    while True:
        print('Starting...')
        thread = threading.Thread(target=lambda:system(comand))
        thread.daemon = True
        thread.start()

        while True:
            print('Waiting for updates...')
            time.sleep(time_wait)

            if check_for_updates(repo):
                print('Update found. Updating...')
                pull(repo)
                print('Update done. Killing comand...')
                thread.join()
                break    


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
    run_comand(comand,time_wait,repo)


    print(inputs)
if __name__ == '__main__':
    main()