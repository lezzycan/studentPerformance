from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    Docthis function will return the list of requirements
    string for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: list[str]
    '''
    requirements = []
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements        
            



setup(
name='mlproject',
version='0.0.1',
author='Olalekan Waheed',
author_email='waheedolalekan23@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'),

)

