
import time
import subprocess
import psutil
from git import Repo
from aurora.repository import check_for_updates,pull


def kill_all_process(proc_pid:int):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()



def exec_repository_actions(comand:str or None,time_wait:int,repo:str):
         
    try:
        repo = Repo(repo)
    except:
        print('Invalid repository path. Exiting...')
        raise Exception('Invalid repository path')
        
    while True:
        print('Starting...')
        if comand:
            process = subprocess.Popen(comand,shell=True)
    
        while True:
            print('Waiting for updates...')
            time.sleep(time_wait)

            #means that there is an update
            if check_for_updates(repo):
                print('Update found. Updating...')
                pull(repo)
                print('Update done. Killing comand...')
                
                # kill the process
                if comand:
                    kill_all_process(process.pid)
                break 