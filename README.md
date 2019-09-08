# robotframework-aws

#### Contributors are welcome. This package is at the beginning of development.
 [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
 ![PyPI](https://img.shields.io/pypi/v/robotframework-aws.svg)
 [![Build Status](https://travis-ci.com/teaglebuilt/robotframework-AWS.svg?branch=master)](https://travis-ci.com/teaglebuilt/robotframework-AWS)
 
![Last Commit](https://img.shields.io/github/last-commit/teaglebuilt/robotframework-AWS)
![License](https://img.shields.io/pypi/l/robotframework-aws)
![Downloads](https://img.shields.io/pypi/dm/robotframework-aws)
[![Coverage Status](https://coveralls.io/repos/github/teaglebuilt/robotframework-AWS/badge.svg?branch=master)](https://coveralls.io/github/teaglebuilt/robotframework-AWS?branch=master)
---------------
A library of keywords for interacting with AWS services in your robot tests. This library covers a variety of AWS services.

[Documentation for Keywords](https://teaglebuilt.github.io/robotframework-AWS/)

____________
___________
#### Attention Contributors
  [Contribution guidelines for this project](CONTRIBUTING.md)

#### Installation

1. Install the package

```
pip install robotframework-aws
```

2. Import Package
  ##### Pass in your AWS Credentials as parameters as shown below.
```
*** Settings ***
Library  AWSLibrary  ${access_key}  ${secret_key}
```

3. Creating a Test Case
   ##### When creating a test case, start with creating a session in AWS for your test.
   ```
   ***Test Case***
   Example Test Case
        Create Session  us-east-1
        Key Should Not Exist  bucky  static/test.html  test.html
        Upload File  bucky  static/test.html  test.html
        Key Should Exist  bucky static/test.html  test.html
        Delete Session  us-east-1
   ```

> ## Session
####  A session is created to use AWS services as a user defining the region and profile is optional.

 - | `Create Session` | region | profile=optional |
 - | `Delete Session` | region | profile=optional |
 - | `Delete All Sessions` |

 > ### S3 
#####  A key represents the path of the file located in the S3 bucket and Object Path represents the local path of the file on your host.

 - | `Get Bucket` | bucket_name |
 - | `Get Object` | bucket_name | object_path |
 - | `Upload File` | bucket_name | object_path | key |
 - | `Download File` | bucket_name | object_path | key |
 - | `Key Should Exist` | bucket_name | object_path | key |
 - | `Key Should Not Exist` | bucket_name | object_path | key |
 - | `Allowed Methods` | array of methods |



> ### Resources
####  Keywords can be used for local functionality that can be used with all services. These are helper methods to validate functionality, existence, and so on.

 - | `Local File Should Exist` | path |
 - | `Local File Should Not Exist` | path |

