from setuptools import setup, find_packages, setup

def get_requirements(file_path: str) -> list[str]:
   from typing import List 
   ''' this function will return the list of requirements '''
   requirements=[]
   with open(file_path) as file_obj:
         requirements = file_obj.readlines()
         requirements = [req.replace("\n","") for req in requirements] # informal way to remove \n from each line
         if '-e .' in requirements:
            requirements.remove('-e .')
   return requirements

        
setup(
    name='mlproject',
    version='0.0.1',
    author='NSG',
    author_email='nsg@example.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)