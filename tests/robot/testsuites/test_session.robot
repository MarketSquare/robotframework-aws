*** Settings ***
Library  Collections
Library  AWSLibrary
Resource  ../resources.robot


*** Variable ***
${REGION}=  us-east-1


*** Test Case ***
Session Exists
    Run Keyword And Expect Error
    ...  No Session
    ...  Get Client  ${REGION}
    Suite Setup
    Get Client  ${REGION}
    Suite Teardown


