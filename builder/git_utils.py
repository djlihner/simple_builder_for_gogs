from subprocess import check_output


def get_branches(repo):
    remote_branches = []
    for ref in repo.git.branch('-r').split('\n  origin/'):
        remote_branches.append(ref)
    remote_branches.pop(0)
    return remote_branches


def get_last_commit_hash():
    return check_output("git log -1 --pretty=format:'%H'").decode().split("\'")[1]
