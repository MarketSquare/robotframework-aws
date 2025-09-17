from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        read_me = f.read()
    return read_me


setup(
    name='robotframework-aws',
    version='1.0.0',
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
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3 >= 1.40.30', 'robotframework >= 6.1.1', 'robotframework-pythonlibcore>=4.4.1']
)
