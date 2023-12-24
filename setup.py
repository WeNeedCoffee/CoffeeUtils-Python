from setuptools import setup, find_packages
import os


def get_version():
    basedir = os.path.dirname(__file__)
    with open(os.path.join(basedir, '.bumpversion.cfg')) as f:
        version = [line.split('=')[1].strip() for line in f.readlines() if line.startswith('current_version = ')][0]
    return version


setup(
    name="coffee-utils",
    version=get_version(),
    packages=find_packages(),
)
