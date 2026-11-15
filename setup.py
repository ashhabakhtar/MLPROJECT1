from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """Read install requirements, ignoring comments and blank lines."""
    with open(file_path) as file_obj:
        requirements = [
            requirement.strip()
            for requirement in file_obj
            if requirement.strip() and not requirement.lstrip().startswith("#")
        ]
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="ASHHAB",
    author_email="akhtarashhab@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)