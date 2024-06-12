# robotframework-aws

AWSLibrary is a testing library for Robot Framework that gives you the ability to use many of the AWS services in your tests. 
This library directly interacts with [Boto 3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).  
Boto is the Amazon Web Services (AWS) SDK for Python. It enables Python developers to create, configure, and manage 
AWS services.

If there is functionality that should be included in this library please create an issue or feel free to contribute.

## Contributors are welcome. This package is at the beginning of development

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
![PyPI](https://img.shields.io/pypi/v/robotframework-aws.svg)
![Last Commit](https://img.shields.io/github/last-commit/MarketSquare/robotframework-aws)
![License](https://img.shields.io/pypi/l/robotframework-aws)
![Downloads](https://img.shields.io/pypi/dm/robotframework-aws)

## Keyword Documentation

---------------

This library covers the AWS services listed in the keywords:

[Documentation of keywords](https://raw.githack.com/MarketSquare/robotframework-aws/master/docs/AWSLibrary.html)

[Pypi](https://pypi.org/project/robotframework-aws/)

---------------

### Installation and use

#### Install the package

```sh
pip install robotframework-aws
```

#### Creating a Test Case

When creating a test case, start with creating a session in AWS for your test

```robotframework
*** Settings ***
Library  AWSLibrary


*** Variables ***
${REGION}    eu-west-1
${BUCKET}    some-bucket-name


*** Test Cases ***
Test Open Connection
    [Setup]    Create Session With Keys    ${REGION}    %{AWS_USER_NAME}    %{AWS_USER_PASS}
    S3 Upload File    ${BUCKET}    new_file.json    ${CURDIR}/local_file.json
    S3 Key Should Exist    ${BUCKET}    new_file.json
    S3 Key Should Not Exist    ${BUCKET}    local_file.json
    ${file_inside_folder}    S3 List Objects    ${BUCKET}    folder_name
    Log List   ${file_inside_folder}
    S3 Download File    ${BUCKET}    new_file.json    ${CURDIR}/new_local_file.json
    S3 Delete File    ${BUCKET}    new_file.json
    [Teardown]    Delete All Sessions
```

### Attention Contributors

  [Contribution guidelines for this project](CONTRIBUTING.md)
