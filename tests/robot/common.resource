*** Settings ***
Library    ${CURDIR}/../../src/AWSLibrary
Library    Collections
Library    OperatingSystem
Variables    data/variables.py

*** Variables ***
${REGION}    us-east-1
${ACCESS_KEY}    dummy
${SECRET_KEY}    dummy
${LOCALSTACK_ENDPOINT}    http://localhost:4566

*** Keywords ***
Create Session And Set Endpoint
    Create Session With Keys    ${REGION}    ${ACCESS_KEY}    ${SECRET_KEY}
    SQS Set Endpoint Url    ${LOCALSTACK_ENDPOINT}    # Point to localstack sqs instance
    S3 Set Endpoint Url    ${LOCALSTACK_ENDPOINT}    # Point to localstack s3 instance
    Dynamo Set Endpoint Url    ${LOCALSTACK_ENDPOINT}    # Point to localstack s3 instance
