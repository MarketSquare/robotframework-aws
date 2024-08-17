*** Settings ***
Library    ${CURDIR}/../../../../src/AWSLibrary
Library    Collections
Library    OperatingSystem
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${REGION}    us-east-1
${ACCESS_KEY}    dummy
${SECRET_KEY}    dummy
${queue}    test-queueName
${invalid_queue}    invalid-queueName


*** Test Cases ***
Send and Recieve Message
    Send Message To SQS    ${queue}    Hello world!
    Sleep    2
    ${messages}    Receive Messages From SQS    ${queue}
    ${dict_message}    Set Variable    ${messages}[0]
    Dictionary Should Contain Key    ${dict_message}    Body
    ${actual_value}    Get From Dictionary    ${dict_message}    Body
    Should Be Equal    ${actual_value}   Hello world!

Invalid Queue Name
    TRY
        Send Message To SQS    ${invalid_queue}    Hello world!
    EXCEPT    AS    ${error}
        Log    ${error}
    END
    Should Be Equal    ${error}    Queue name '${invalid_queue}' not found.
    
    
Delete Messages
    Delete All Messages In SQS    ${queue}
    ${messages}    Receive Messages From SQS    ${queue}
    ${count}    Get Length    ${messages}
    Should Be Equal As Integers    ${count}   0


*** Keywords ***
Create Session And Set Endpoint
    Create Session With Keys    ${REGION}    ${ACCESS_KEY}    ${SECRET_KEY}
    SQS Set Endpoint Url    http://localhost:4566    # Point to localstack sqs instance
