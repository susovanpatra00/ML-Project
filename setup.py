from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "") for req in requirements] 

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='ML-Project',
    version='0.0.1',
    author='Susovan',
    author_email='susovanpatra00@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)






# 'setup.py' is a build script for setuptools or distutils, which are Python libraries used to distribute and 
# install Python packages. It is a key file when you are creating a Python package to distribute to others, 
# whether through the Python Package Index (PyPI), internally within an organization, or for personal use.
#
# The setup.py script contains information about your package such as its name, version, description, dependencies, 
# and more, which setuptools or distutils use to package and install the Python package.
#
# Example :
# from setuptools import setup, find_packages
#
# setup(
#     name='example_package',
#     version='0.1',
#     packages=find_packages(),
#     description='An example Python package',
#     long_description=open('README.md').read(),
#     url='http://example.com',
#     author='Your Name',
#     author_email='your.email@example.com',
#     license='MIT',
#     install_requires=[
#         # List of dependencies
#     ],
# )
