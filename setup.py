from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()  # ✅ Read line by line
        requirements = [req.strip() for req in requirements if req.strip()]  # ✅ Remove empty lines and newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements





setup(
    name='my_project',
    version='0.0.1',
    description='A simple ML project',
    author='Salman',
    author_email='salmanalam8083@gmail.com',
    url='https://github.com/MDSALMANALAM/1.-ML-Project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt')
)