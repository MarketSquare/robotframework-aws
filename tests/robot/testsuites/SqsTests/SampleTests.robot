*** Settings ***
Library    AWSLibrary
Library    Collections
Library    SeleniumLibrary
Suite Setup    Create Session With Keys  ${REGION}  ${ACCESS_KEY}  ${SECRET_KEY}
Suite Teardown    Delete All Sessions

*** Variables ***
${REGION}    us-east-1
${ACCESS_KEY}    dummy
${SECRET_KEY}    dummy


*** Test Cases ***

Send and Recieve Message
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
    Send Message To SQS    test-queueName    Hello world!
    Sleep    2
    ${messages}    Receive Messages From SQS    test-queueName
    ${dict_message}    Set Variable    ${messages}[0]
    Dictionary Should Contain Key    ${dict_message}    Body
    ${actual_value}    Get From Dictionary    ${dict_message}    Body
    Should Be Equal    ${actual_value}   Hello world!

Invalid Queue Name
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
    TRY
        Send Message To SQS    invalid-queueName    Hello world!
    EXCEPT    Queue name 'invalid-queueName' not found.
        Log    caught exception
    END
    
Delete Messages
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
    Delete All Messages In SQS    test-queueName
    ${messages}    Receive Messages From SQS    test-queueName
    ${count}    Get Length    ${messages}
    Should Be Equal As Integers    ${count}   0

