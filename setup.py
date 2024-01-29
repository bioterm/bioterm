import os

from setuptools import find_packages
from setuptools import setup


def load_requirements(filename="requirements.txt"):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_dir, filename)
    with open(full_path, "r") as file:
        return file.read().splitlines()


setup(
    name="bioterm",
    version="0.0.1",
    packages=find_packages(exclude=["tests", "tests.*", "deployment", "deployment.*"]),
    install_requires=load_requirements(),
    package_data={
        "bioterm": ["common/core/logger_conf.yaml"],
    },
)
