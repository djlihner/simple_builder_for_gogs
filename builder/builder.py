import os
import logger


class BuildEnvironment(object):

    def __init__(self):
        self.project_dir = os.path.abspath('..\\test_build')
        self.build_report_dir = os.path.join(self.project_dir, 'build_output\\reports')
        self.pylint_report_path = os.path.join(self.build_report_dir, 'pylint_report.txt')
        self.pylint_suppress_csv = 'C0111,R0903,W0232,R0201,W0511'


build_env = BuildEnvironment()
log = logger.get_logger()


def deploying_build(url, branch):
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
    os.system('pylint --max-line-length=120 --output-format=parseable --disable={0} {1} >> {2}'.format(
        build_env.pylint_suppress_csv,
        build_env.project_dir,
        build_env.pylint_report_path))
    log.info("Done! Report created in {}".format(build_env.build_report_dir))
