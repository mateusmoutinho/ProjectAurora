
import time
import subprocess
import psutil
from git import Repo
from aurora.repository import check_for_updates,pull
from aurora.log import treat_log


def kill_process(proc_pid:int):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()



def run_comands(acumulated_log:list,quiet:bool,comands:list or None,time_wait:int,repo:str):
         
    try:
        repo = Repo(repo)
    except:
        treat_log(acumulated_log,'Invalid repository path',quiet,error=True)
        raise Exception('Invalid repository path',repo)
        

    while True:
        treat_log(acumulated_log,'Checking for updates...',quiet)
        all_process = []
        for comand in comands:
            treat_log(acumulated_log,f'Running comand: {comand}',quiet)
            process_created = subprocess.Popen(comand,shell=True) 
            all_process.append(process_created)
    
        while True:
            
            time.sleep(time_wait)

            #means that there is an update
            if check_for_updates(repo):
                treat_log(acumulated_log,'Update found. Pulling...',quiet)
                pull(repo)
                treat_log(acumulated_log,'Update pulled. Killing all processes...',quiet)
                
                
                for process in all_process:
                    kill_process(process.pid)
                break 