
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

    try:
        repo = Repo(repository_path)
    except:
        print_if_not_quiet(quiet,'Invalid repository path')
        raise Exception('Invalid repository path',repo)
        
    while True:
        all_process = []
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