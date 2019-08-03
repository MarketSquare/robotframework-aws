from setuptools import setup, find_packages
from os.path import abspath, dirname, join
import codecs



def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='robotframework-aws',
    version='0.0.3',
    author="Dillan Teagle",
    author_email="softwaredeveloper@dillanteagle.me",
    description="A python package to test AWS services in Robot Framework",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://www.github.com/teaglebuilt/robotframework-aws",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3 >= 1.9.1', 'robotframework >= 3.1.2']
)