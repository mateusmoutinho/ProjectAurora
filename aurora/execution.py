
import time
import subprocess
import psutil
from git import Repo
from aurora.git_functions import check_for_updates,resset_and_pull
from aurora.general import print_if_not_quiet

def kill_process(proc_pid:int):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()



def generate_repository_actions(repository_props:dict,quiet:bool):
    """Generate the actions for the repository."""
    repository_path = repository_props['repository']
    comands = repository_props['comands']
    time_wait = repository_props['timewait']
    before = repository_props['before']
    time_out_before = repository_props['timeout_before']
    #run the before comand and wait for it to finish

        
    try:
        repo = Repo(repository_path)
    except:
        print_if_not_quiet(quiet,'Invalid repository path')
        raise ValueError('Invalid repository path')
        
    while True:
        all_process = []
        if before:
            before_process = subprocess.Popen(before,shell=True) 
            for i in range(time_out_before):
                time.sleep(1)
                if before_process.poll() != None:
                    break
            if before_process.poll() == None:
                kill_process(before_process.pid)
                print_if_not_quiet(quiet,'Before comand timeout')
                break
    

        for comand in comands:
            
            process_created = subprocess.Popen(comand,shell=True) 
            all_process.append(process_created)
    
        while True:
            
            time.sleep(time_wait)

            #means that there is an update
            if check_for_updates(repo):
                print_if_not_quiet(quiet,'Update found. Pulling...')
                resset_and_pull(repo)
                print_if_not_quiet(quiet,'Update pulled. Killing processes...') 
                for process in all_process:
                    kill_process(process.pid)
                break 