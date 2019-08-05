*** Settings ***
Library  AWSLibrary


*** Variable ***
${REGION}=  us-east-1


*** Keywords ***
Suite Setup
    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}

Suite Teardown
    Delete All Sessions