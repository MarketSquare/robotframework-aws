*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${QUEUE_NAME}    test-queueName
${INVALID_QUEUE}    invalid-queueName


*** Test Cases ***
Send and Recieve Message
    [Tags]    sqs
    Send Message To SQS    ${QUEUE_NAME}    Hello world!
    Sleep    2
    ${messages}    Receive Messages From SQS    ${QUEUE_NAME}
    ${dict_message}    Set Variable    ${messages}[0]
    Dictionary Should Contain Key    ${dict_message}    Body
    ${actual_value}    Get From Dictionary    ${dict_message}    Body
    Should Be Equal    ${actual_value}   Hello world!

Invalid Queue Name
    [Tags]    sqs
    TRY
        Send Message To SQS    ${INVALID_QUEUE}    Hello world!
    EXCEPT    AS    ${error}
        Log    ${error}
    END
    Should Be Equal    ${error}    Queue name '${INVALID_QUEUE}' not found.
    
Delete Messages
    [Tags]    sqs
    Delete All Messages In SQS    ${QUEUE_NAME}
    ${messages}    Receive Messages From SQS    ${QUEUE_NAME}
    ${count}    Get Length    ${messages}
    Should Be Equal As Integers    ${count}   0
