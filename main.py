from cli_args_system import Args
from git import Repo
from os import getcwd
from sys import exit



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
    """Execute pull on the repo"""
    origin = repo.remotes.origin
    origin.pull()


def get_inputs()->dict:
    args = Args()
    repo = args.flag_str('repo','r','repository')
    if not repo:
        repo = getcwd()
    exec = args.flag_str('exec','e','executable')

    time = args.flag_str('time','t','time')
    if not time:
        time = 10
    else:
        try:
            time = int(time)     
        except:
            print('Invalid time specified. Exiting...')
            exit(1)

    if not exec:
        print('No executable specified. Exiting...')
        exit(1)
    return {
        'repository':repo,
        'executable':exec,
        'time':time
    }    




def main():
    inputs = get_inputs()
    repository_path = inputs['repository']
    time_wait = inputs['time']
    executable = inputs['executable']

    try:
        repo = Repo(repository_path)
    except:
        print('Invalid repository path. Exiting...')
        exit(1)


    if check_for_updates(repo):
        print('Update found. Updating...')
        pull(repo)
 

    print(inputs)
if __name__ == '__main__':
    main()