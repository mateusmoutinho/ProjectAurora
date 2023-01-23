
import time
import subprocess
import psutil
from git import Repo
from repository import check_for_updates,pull

def kill_all_process(proc_pid:int):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()



def run_comand(comand:str,time_wait:int,repo:Repo):
    while True:
        print('Starting...')
        process = subprocess.Popen(comand,shell=True)
    
        while True:
            print('Waiting for updates...')
            time.sleep(time_wait)

            if check_for_updates(repo):
                print('Update found. Updating...')
                pull(repo)
                print('Update done. Killing comand...')
                
                # kill the process
                kill_all_process(process.pid)
                break 