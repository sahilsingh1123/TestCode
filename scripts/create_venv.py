"""
Pre-requisite - must have pip installed.
venv -- you can pass the virtualenv name or name with path = ex ( -vn virtualenv_test_name | -vn /user/test/projects/virtualenv_name )
requirement.txt -- You can pass the req.txt file with name or name with path = ex ( -rq requirement.txt | -rq /user/test/Documents/requirement.txt )
example to run -- python3.9 create_venv.py -vn test_venv -rq requirements.txt

Note: If no arguments passed then default virtual-env name will be 'venv'. All the arguments are optional.
"""

import subprocess
import os
import pkg_resources
import argparse
import platform
import sys

CWD = os.getcwd()
print('Current Directory: {0}'.format(CWD))
CHECK_PACKAGES = ['pip', 'virtualenv']
OS_NAME = platform.system()
PYTHON_VER_NUM = platform.python_version()
VERSION_INFO = sys.version_info
PYTHON_VERSION = 'python' + str(VERSION_INFO[0]) + '.' + str(VERSION_INFO[1])
print(PYTHON_VERSION)


def main(venv_name, requirement_path=None):
    for package in CHECK_PACKAGES:
        try:
            dist = pkg_resources.get_distribution(package)
            print('{} ({}) is found'.format(dist.key, dist.version))
        except pkg_resources.DistributionNotFound:
            print('{0} is NOT installed.\n Installing {0}....'.format(package))
            if package != 'pip':
                subprocess.call('{0} -m pip install --user {1}'.format(PYTHON_VERSION, package), shell=True, stdout=True, stderr=True)
    subprocess.call('{0} -m virtualenv {1}'.format(PYTHON_VERSION, venv_name), shell=True, stdout=True, stderr=True)
    if requirement_path:
        subprocess.call('{0}/{1}/bin/python -m pip install -r {2}'.format(CWD, venv_name, requirement_path), shell=True, stdout=True, stderr=True)


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Create the Virtual env")
    argparser.add_argument('-vn', '--venv_name', help="Venv Name", default="venv", required=False)
    argparser.add_argument('-rq', '--requirement_path', help="requirement.txt path", required=False)

    args = argparser.parse_args()
    d = vars(args)
    main(**d)
