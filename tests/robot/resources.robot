*** Settings ***
Library  AWSLibrary


*** Variable ***
${REGION}=  us-east-1


*** Keywords ***
Test Setup
    Create Session With Keys  ${REGION}

Test Teardown
    Delete All Sessions