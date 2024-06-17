from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name='robotframework-aws',
    version='0.1.0',
    author="Dillan Teagle",
    author_email="softwaredeveloper@dillanteagle.me",
    description="A python package to test AWS services in Robot Framework",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/MarketSquare/robotframework-aws",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3 >= 1.34.125', 'robotframework >= 6.1.1', 'robotframework-pythonlibcore>=4.4.1']
)
