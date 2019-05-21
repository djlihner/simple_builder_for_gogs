import os
import time
import git

from builder import git_utils
from builder import logger


class BuildEnvironment(object):

    def __init__(self):
        self.project_dir = os.path.abspath('..\\test_build')
        self.build_report_dir = os.path.join(self.project_dir, 'build_output\\reports')
        self.pylint_report_path = os.path.join(self.build_report_dir, 'pylint_report.txt')
        self.pylint_suppress_csv = 'C0111,R0903,W0232,R0201,W0511'


build_env = BuildEnvironment()
log = logger.get_logger()
commits = dict()


def check_push_thread(url):
    __clean_build_directories()
    repo = git.Repo.clone_from(url, build_env.project_dir)

    while True:
        branches = git_utils.get_branches(repo)

        for branch in branches:
            repo.git.checkout(branch)
            commits[branch] = repo.head.commit

        time.sleep(10)

        os.chdir(build_env.project_dir)
        os.system("git pull")

        for branch in branches:
            repo.git.checkout(branch)
            log.info("Searching new commits in {} {}".format(url, branch))

            past_commit_sha = str(commits[branch])
            present_commit_sha = git_utils.get_last_commit_hash()

            if not past_commit_sha == present_commit_sha:
                log.warning("Sha past commit {} was not equal {}".format(past_commit_sha, present_commit_sha))
                commits[branch] = git_utils.get_last_commit_hash()
                deploying_build(url, branch)


def deploying_build(url, branch="master"):
    __clean_build_directories()
    log.info("Deploying branch - {} into {}".format(branch, build_env.project_dir))
    os.system('git clone -b {} {} {}'.format(branch, url, build_env.project_dir))
    __run_code_analysis()


def __clean_build_directories():
    log.info("Clean up build directories was started")
    if os.path.exists(build_env.project_dir):
        os.system('rmdir /S /Q "{}"'.format(build_env.project_dir))
        log.info("Successfully!")
    else:
        log.warning("Old build was not found")


def __run_code_analysis():
    log.info("Code analysis was started")

    if not os.path.exists(build_env.build_report_dir):
        os.makedirs(build_env.build_report_dir)

    os.chdir(build_env.project_dir)
    os.system('pylint --max-line-length=120 --output-format=parseable --disable={} {} >> {}'.format(
        build_env.pylint_suppress_csv,
        build_env.project_dir,
        build_env.pylint_report_path))
    log.info("Done! Report created in {}".format(build_env.build_report_dir))
