
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



def exec_repository_actions(comands:list or None,time_wait:int,repo:str):
         
    try:
        repo = Repo(repo)
    except:
        print('Invalid repository path. Exiting...')
        raise Exception('Invalid repository path')
        
    while True:
        print('Starting...')
        all_process = []
        for comand in comands:
            process_created = subprocess.Popen(comand,shell=True) 
            all_process.append(process_created)
    
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
                    for process in all_process:
                        kill_all_process(process.pid)
                break 