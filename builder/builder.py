import os


class BuildEnvironment(object):

    def __init__(self):
        self.project_dir = os.path.abspath('../test_build')
        self.virtualenv_dir = os.path.join(self.project_dir, 'env')
        self.build_report_dir = os.path.join(self.project_dir, 'build_output/reports')
        self.pylint_report_path = os.path.join(self.build_report_dir, 'pylint_report.txt')
        self.pylint_suppress_csv = 'C0111,R0903,W0232,R0201,W0511'


build_env = BuildEnvironment()


def clone_project(url, branch):
    if not os.path.exists(build_env.project_dir):
        os.system('git clone -b {} {} {}'.format(branch, url, build_env.project_dir))


def code_analysis():
    if not os.path.exists(build_env.build_report_dir):
        os.makedirs(build_env.build_report_dir)

    os.chdir(build_env.project_dir)
    os.system('pylint --max-line-length=120 --output-format=parseable --disable={0} {1} >> {2}'.format(
        build_env.pylint_suppress_csv,
        build_env.project_dir,
        build_env.pylint_report_path))


def clean_project():
    if os.path.exists(build_env.build_report_dir):
        os.system('rmdir /S /Q "{}"'.format(build_env.project_dir))
