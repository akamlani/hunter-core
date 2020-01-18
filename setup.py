from setuptools import setup
from setuptools import find_packages

### development mode, symlinks and editable
# python setup.py develop
# pip    install -e .
setup(
    name='hunter-workflows',
    version='0.0.1',
    packages=find_packages(),
    description='Encapsulation of Workflows for Data Science',
    license='MIT',
    author='Ari Kamlani',
    author_email='akamlani@gmail.com',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],

)

