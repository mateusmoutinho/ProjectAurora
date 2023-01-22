

from git import Repo

def check_for_updates(repo_path)->bool:
    """Check if the local repo is up to date with the remote repo."""
    repo = Repo(repo_path)
    current_hash = repo.head.object.hexsha
    origin = repo.remotes.origin
    origin.fetch()
    remote_hash = origin.refs.main.commit.hexsha
    return current_hash != remote_hash


def main():
    pass 



