*** Settings ***
Library    ${CURDIR}/../../src/AWSLibrary
Library    OperatingSystem


*** Variables ***
${REGION}    us-east-1


*** Test Cases ***
Test Setup
    Create Session With Keys    ${REGION}    test    test
    ${files}    List Objects    sample-bucket    endpoint_url=http://localhost:4566/
    Log    ${files}    warn
    Delete All Sessions