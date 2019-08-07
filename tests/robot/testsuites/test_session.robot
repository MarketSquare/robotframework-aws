*** Settings ***
Library  Collections
Library  AWSLibrary
Resource  ../resources.robot


*** Variable ***
${REGION}=  us-east-1


*** Test Case ***
Session Exists
    Test Setup
    Test Teardown
