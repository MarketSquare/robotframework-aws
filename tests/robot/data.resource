*** Settings ***
Library    ${CURDIR}/../../src/AWSLibrary
Library    Collections
Library    OperatingSystem

*** Variables ***
${REGION}    us-east-1
${ACCESS_KEY}    dummy
${SECRET_KEY}    dummy


*** Keywords ***
Create Session And Set Endpoint
    Create Session With Keys    ${REGION}    ${ACCESS_KEY}    ${SECRET_KEY}
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
    S3 Set Endpoint Url    http://localhost:4566    # Point to localstack s3 instance
