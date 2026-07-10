from setuptools import *
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(file_path:str)->List[str]:

    '''
    this Function will return a list of requiremet for the projects   
    '''
    requiremets=[]
    with open(file_path) as file_obj:
        requiremets=file_obj.readlines()
        requiremets=[req.replace("\n","") for req in requiremets]

    if HYPEN_E_DOT in requiremets:
        requiremets.remove(HYPEN_E_DOT)
    
    return requiremets


setup(name="Machine Learning Project-1",
      version="0.0.1",
      author="Aditya72",
      author_email="jamdaraditya26@gmail.com",
      packages=find_packages(),
      install_requires=get_requirements("requirements.txt")
      )
