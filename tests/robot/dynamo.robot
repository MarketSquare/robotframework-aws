*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${TABLE_NAME}    global


*** Test Cases ***
Test Put And Query Item
    [Tags]    dynamo
    Dynamo Put Item    ${TABLE_NAME}    ${ITEM_CODE_01}
    ${result}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Should Be Equal    ${result}[0]    ${ITEM_CODE_01}

Test Delete And Update Key
    [Tags]    dynamo
    [Setup]    Dynamo Put Item    ${TABLE_NAME}    ${ITEM_CODE_01}
    Dynamo Remove Key    ${TABLE_NAME}    id    code01    factory
    ${result_delete}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Dictionary Should Not Contain Key    ${result_delete}[0]    factory
    Dynamo Update Key    ${TABLE_NAME}    id    code01    quantity    ${10}
    Dynamo Update Key    ${TABLE_NAME}    id    code01    active    ${False}
    Dynamo Update Key    ${TABLE_NAME}    id    code01    name    new name
    ${result_update}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Should Be Equal    ${result_update}[0][quantity]    ${10}
    Should Be Equal    ${result_update}[0][active]    ${False}
    Should Be Equal    ${result_update}[0][name]    new name
