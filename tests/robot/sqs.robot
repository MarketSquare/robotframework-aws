*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${QUEUE_NAME}       test-queueName
${INVALID_QUEUE}    invalid-queueName


*** Test Cases ***
Send and Receive Message
    [Tags]    sqs
    Sqs Send Message    ${QUEUE_NAME}    Hello world!
    ${messages}    Sqs Receive Messages    ${QUEUE_NAME}
    ${dict_message}    Set Variable    ${messages}[0]
    Dictionary Should Contain Key    ${dict_message}    Body
    ${actual_value}    Get From Dictionary    ${dict_message}    Body
    Should Be Equal    ${actual_value}   Hello world!
    [Teardown]    Sqs Delete All Messages    ${QUEUE_NAME}

Send and Receive Messages
    [Tags]    sqs
    ${messages_number}    Set Variable    ${5}
    FOR    ${index}    IN RANGE    1    ${messages_number}+1
        Sqs Send Message    ${QUEUE_NAME}    Message 0${index}
    END
    ${messages}    Sqs Receive Messages    ${QUEUE_NAME}
    ${messages_len}    Get Length    ${messages}
    Should Be Equal As Integers    ${messages_len}   ${messages_number}
    [Teardown]    Sqs Delete All Messages    ${QUEUE_NAME}

Invalid Queue Name
    [Tags]    sqs
    TRY
        Sqs Send Message    ${INVALID_QUEUE}    Hello world!
    EXCEPT    AS    ${error}
        Log    ${error}
    END
    Should Be Equal    ${error}    Queue name '${INVALID_QUEUE}' not found.
    
Delete Messages
    [Tags]    sqs
    Sqs Delete All Messages    ${QUEUE_NAME}
    ${messages}    Sqs Receive Messages    ${QUEUE_NAME}    wait_time=5
    ${messages_len}    Get Length    ${messages}
    Should Be Equal As Integers    ${messages_len}   0
