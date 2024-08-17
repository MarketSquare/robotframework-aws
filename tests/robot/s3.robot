*** Settings ***
Library    ${CURDIR}/../../src/AWSLibrary
Library    Collections
Library    OperatingSystem
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${REGION}    us-east-1
${ACCESS_KEY}    dummy
${SECRET_KEY}    dummy


*** Test Cases ***
Test S3
	[Tags]    s3
	${objects}    S3 List Objects    test-bucket
	Log    ${objects}    warn
	S3 Upload File    test-bucket    s3_file.txt    ${CURDIR}/local_file.txt
	${objects}    S3 List Objects    test-bucket
	Log    ${objects}    warn
	

*** Keywords ***
Create Session And Set Endpoint
    Create Session With Keys    ${REGION}    ${ACCESS_KEY}    ${SECRET_KEY}
    S3 Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
