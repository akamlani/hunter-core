from setuptools import setup
from setuptools import find_packages, find_namespace_packages
import sys 

from hunter import __version__ 

###############################################################################
if sys.version_info < (3, 5):
	print('{} requires Python 3.5 or later.'.format('hunter-core'))

###############################################################################

# list required packaged
REQUIRED_PACKAGES = [
]


### development mode, symlinks and editable
# python setup.py develop
# pip    install -e .
setup(
    name='hunter-core',
    version=__version__,            
    description='Encapsulation of Workflows for Machine Learning/Deep Learning',
    keywords='deep learning',

    license='MIT',
    author='Ari Kamlani',
    author_email='akamlani@gmail.com',
    classifiers=['License :: OSI Approved :: MIT License',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence'],

    # what is packaged here
    install_requires=REQUIRED_PACKAGES,
    packages=find_namespace_packages(include=["hunter.*"]),
   	# What to include
   	package_data={
        '': ['*.txt', '*.rst', '*.md']
    },
    # Testing
    test_suite='tests',
   	tests_require=[
        'pytest',
    ],
)


