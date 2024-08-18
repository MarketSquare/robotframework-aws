# Development environment

Feel free to create issues for ideas for new functionality with other aws services

We are working to create an environment with tests in localstack https://github.com/localstack/localstack if you have 
experience with this tool and time, any help will be appreciated.

## Contributing to RobotFramework-AWS

Thank you for considering contributing to a library for interacting with AWS services in RobotFramework 
for test automation.

Configure your environment as desired, the requirements are in the requirements.txt file

```sh
pip install -r requirements.txt
```

## Testing

### Localstack

For now, we have inside the folder localstack the docker compose file and in the init-aws.sh the commands to send
for localstack.

To start localstack just run inside localstack folder:
```sh
docker-compose up
```
Then you can use inside robot, the endpoint http://localhost:4566

### Robot Framework

The tests suites are inside tests/robot folder

The common variables, keywords and libraries should be in common.resource file. The tests suites have the 
aws module name like s3.robot or sqs.robot then we can run it separately.

Any extra file like txt, json, csv or similar should be inside data folder.

The robot files should import only the common.resource.

```robotframework
*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions
```

All the libraries import should be in common.resource, as the suite setup.

```robotframework
*** Settings ***
Library    ${CURDIR}/../../src/AWSLibrary
Library    Collections
Library    OperatingSystem


*** Keywords ***
Create Session And Set Endpoint
    Create Session With Keys    ${REGION}    ${ACCESS_KEY}    ${SECRET_KEY}
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
    S3 Set Endpoint Url    http://localhost:4566    # Point to localstack s3 instance
```

### TO-DO

- [ ]  Create CloudWatch and DynamoDB in localstack and create robot tests
- [ ]  Add more services in library and in localstack
- [ ]  Add robot tests for this new services
- [ ]  Create GitHub actions to run the tests in push and merges.
