import imp
from setuptools import setup, find_packages

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "request>=2"]

setup(
    name='algobottrading',
    version=0.0.1
    author='Anirban Das'
    author_email='anirbandas59@outlook.com'
    description='A package to run algorithmic bot trading'
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/anirbandas59/algobottrading',
    requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)
