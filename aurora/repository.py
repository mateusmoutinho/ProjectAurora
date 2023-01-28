from git import Repo



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
