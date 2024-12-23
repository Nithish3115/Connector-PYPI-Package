from setuptools import setup, find_packages
from typing import List
import os

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

HYPEN_E_DOT='-e .'
def get_requirement(file_path:str)->List[str]:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

__version__ = "0.0.5"
REPO_NAME = "Connector-PYPI-Package"
PKG_NAME= "Monogodb-Connect-automation"
AUTHOR_USER_NAME = "Nithish3115"
AUTHOR_EMAIL = "nithish031105@gmail.com"

setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["pymongo","pymongo[srv]","dnspython","pandas","numpy","ensure","pytest","tox","tox-gh-actions"]
)