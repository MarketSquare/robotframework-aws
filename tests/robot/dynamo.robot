*** Settings ***
Resource    common.resource
Suite Setup    Create Session And Set Endpoint
Suite Teardown    Delete All Sessions


*** Variables ***
${TABLE_NAME}     storage
${TABLE_MUSIC}    music


*** Test Cases ***
Test Put And Query Item
    [Tags]    dynamo
    Dynamo Put Item    ${TABLE_NAME}    ${ITEM_CODE_01}
    ${result}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    ${result_len}    Get Length    ${result}
    Should Be Equal As Integers    ${result_len}    1
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

Test Delete Item
    [Tags]    dynamo
    [Setup]    Dynamo Put Item    ${TABLE_NAME}    ${ITEM_CODE_01}
    ${result}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Should Not Be Empty    ${result}
    Dynamo Delete Item    ${TABLE_NAME}    id    code01
    ${result_delete}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Should Be Empty    ${result_delete}

Test Insert New Key
    [Tags]    run
    [Setup]    Dynamo Put Item    ${TABLE_NAME}    ${ITEM_CODE_01}
    ${result}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Dictionary Should Not Contain Key    ${result}[0]    new_code
    ${new_item}    Copy Dictionary    ${result}[0]    deepcopy=${True}
    Set To Dictionary    ${new_item}    new_code=ABCD
    Dynamo Put Item    ${TABLE_NAME}    ${new_item}
    ${result_update}    Dynamo Query Table    ${TABLE_NAME}    id    code01
    Dictionary Should Contain Key    ${result_update}[0]    new_code

Test Put And Query Item With Sort Key
    [Tags]    dynamo
    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_01}
    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_02}
    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_03}
    ${result_list}    Dynamo Query Table    ${TABLE_MUSIC}    Artist    Black Sabbath
    ${result_len}    Get Length    ${result_list}
    Should Be Equal As Integers    ${result_len}    3
    List Should Contain Value    ${result_list}    ${MUSIC_01}
    List Should Contain Value    ${result_list}    ${MUSIC_02}
    List Should Contain Value    ${result_list}    ${MUSIC_03}
    ${result}    Dynamo Query Table    ${TABLE_MUSIC}    Artist    Black Sabbath    SongTitle    Paranoid
    ${result_len}    Get Length    ${result}
    Should Be Equal As Integers    ${result_len}    1
    Should Be Equal    ${result}[0]    ${MUSIC_02}

Test Delete And Update Key With Sort Key
    [Tags]    dynamo
    [Setup]    Run Keywords    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_01}
    ...    AND    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_02}
    ...    AND    Dynamo Put Item    ${TABLE_MUSIC}    ${MUSIC_03}
    Dynamo Remove Key    ${TABLE_MUSIC}    Artist    Black Sabbath    Year
    ...    sort_key=SongTitle    sort_value=War Pigs
    ${result_delete}    Dynamo Query Table    ${TABLE_MUSIC}    Artist    Black Sabbath    SongTitle    War Pigs
    Dictionary Should Not Contain Key    ${result_delete}[0]    Year
    Dynamo Update Key    ${TABLE_MUSIC}    Artist    Black Sabbath    Year    ${2012}
    ...    sort_key=SongTitle    sort_value=Paranoid
    Dynamo Update Key    ${TABLE_MUSIC}    Artist    Black Sabbath    Album    Paranoid Remaster
    ...    sort_key=SongTitle    sort_value=Paranoid
    ${result_update}    Dynamo Query Table    ${TABLE_MUSIC}    Artist    Black Sabbath    SongTitle    Paranoid
    Should Be Equal    ${result_update}[0][Year]    ${2012}
    Should Be Equal    ${result_update}[0][Album]    Paranoid Remaster
